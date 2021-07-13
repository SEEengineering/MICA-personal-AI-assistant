import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time
import MICA_ai


API_KEY = "tPz27Cro_8T7"
PROJECT_TOKEN = "txAUJg-7Paz9"
RUN_TOKEN = "tn7t3ygcCW5C"


class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.data = self.get_data()

	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		try:
			data = json.loads(response.text)
			return data
		except ValueError:
    			print("Response content is not valid JSON")

	def get_total_cases(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Coronavirus Cases:":
				return content['value']

	def get_total_deaths(self):
		data = self.data['total']

		for content in data:
			if content['name'] == "Deaths:":
				return content['value']

		return "0"

	def get_country_data(self, country):
		data = self.data["country"]

		for content in data:
			if content['name'].lower() == country.lower():
				return content

		return "0"

	def get_list_of_countries(self):
		countries = []
		for country in self.data['country']:
			countries.append(country['name'].lower())

		return countries

	def update_data(self):
		response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

		def poll():
			time.sleep(0.1)
			old_data = self.data
			while True:
				new_data = self.get_data()
				if new_data != old_data:
					self.data = new_data
					print("Data updated")
					MICA_ai.speak("ok sir, i have updated")
					break
				time.sleep(5)


		t = threading.Thread(target=poll)
		t.start()


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = 0.6
		r.phrase_threshold = 0.290
		r.energy_threshold = 368
		audio = r.listen(source)
		
		said = ""

		try:
			said = r.recognize_google(audio)
		except Exception as e:
			print("Exception:", str(e))
			MICA_ai.speak('Could u please say that again ...')

	return said.lower() 
		
def main():
	
	data = Data(API_KEY, PROJECT_TOKEN)
	MICA_ai.speak("Starting prerequisites. This may take a moment! one moment.........")
	print("Starting prerequisites. This may take a moment! one moment.........")
	data.update_data()
	print("Started search")
	MICA_ai.speak("started searching coronovirus info")
	print("started searching coronovirus info")
	
	END_PHRASE = "stop" or "end" or "thank you" or "end search" or "that's all" or "that's it" or "exit"
	country_list = data.get_list_of_countries()

	TOTAL_PATTERNS = {
					re.compile("[\w\s]+ total [\w\s]+ cases"):data.get_total_cases,
					re.compile("[\w\s]+ total cases"): data.get_total_cases,
                    re.compile("[\w\s]+ total [\w\s]+ deaths"):data.get_total_deaths,
                    re.compile("[\w\s]+ total deaths"):data.get_total_deaths
					}

	COUNTRY_PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
                    re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths']
					}

	UPDATE_COMMAND = "update"

	while True:
		print("Listening...")
		text = get_audio()
		print(text)
		result = None

		for pattern, func in COUNTRY_PATTERNS.items():
			if pattern.match(text):
				words = set(text.split(" "))
				for country in country_list:
					if country in words:
						result = func(country)
						break

		for pattern, func in TOTAL_PATTERNS.items():
			if pattern.match(text):
				result = func()
				break

		if text == UPDATE_COMMAND:
			result = "Data is being updated. This may take a moment"
			data.update_data()
			

		if result:
			MICA_ai.speak(result)
			print(result)

		if text.find(END_PHRASE) != -1:  # stop loop
			MICA_ai.speak("ending corona search")
			print("Exit")
			break

