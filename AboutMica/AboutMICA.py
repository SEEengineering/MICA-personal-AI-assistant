import platform 
import MICA_ai

info = {} 

def personal():
    MICA_ai.speak(
        "I am MICA, Mack's Inteligent Companion Assistant, version 1.0. I am a Desktop Based AI Assistant created and developed by mcharrison dorian. I was created using Python with visual studio code. I am a virtual assistant A I made in python for the windows platforms. i have multiple" 
        + "functionalities such as telling the time, sending emails, retriving current news reports, retrieving information through web scraping, machine learning and more."
        + "My purpose is to provide human-like interactions with software and offer decision support for specific tasks."
    )
    MICA_ai.speak("Now i hope you know me. i am here to offer any assistance")

def platDetails():
    
    platform_details = platform.platform() 
    info["platform details"] = platform_details 
    MICA_ai.speak("the platform you are using is" + platform_details)

def system():
    
    system_name = platform.system() 
    info["system name"] = system_name 
    MICA_ai.speak("the system you are using is " + system_name)
  
def architecture():
    architecture_details = platform.architecture()
    info["architectural detail"] = architecture_details 
    MICA_ai.speak("the architecture of this pc is ")
    MICA_ai.speak(architecture_details)

