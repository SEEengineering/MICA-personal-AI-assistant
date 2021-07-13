import wikipedia
import webbrowser
import requests
import datetime
import calendar
#import stormApp
from googlesearch import search

def searchonWiki(query):
    return wikipedia.summary(query,sentences='2')

def openGoogle():
    webbrowser.open('www.google.com')
    return

def openYoutube():
    webbrowser.open('www.youtube.com')

    return

def Googlesearch(query = "What is python ?"):
    tabUrl = "http://google.com/?#q="
    webbrowser.open(tabUrl + query , new= 2)
    #links = getLinksfromgoogle(query)
    # while True :
    #     query = stormApp.get_audio().lower()
    #
    #     if 'close chrome' in query :
    #         os.system("taskkill /f /im " + "chrome.exe")
    #         break
    #     else :
    #         continue
    return

def getLinksfromgoogle(query):
    links = []
    for link in search(query, num=10 ,stop =10 ):
        print(link)
        links.append(link)
    return links




def getDate():
    now = datetime.datetime.now()
    my_date =datetime.datetime.today()
    weakday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    MONTHS = ['January', 'February' , 'March' , 'April' , 'May' , 'June' ,
                   'July' , 'August' , 'September' , 'October' , 'November' ,'December']

    ordinalNumbers = ['1st' , '2nd' , '3rd' , '4th' , '5th ', '6th' , '7th' , '8th' , '9th' , '10th' , '11th',
                      '12th' , '13th' , '14th' , '15th' , '16th' , '17th' ,'18th' , '19th' , '20th' , '21st' ,
                      '22nd', '23rd' , '24th' , '25th' , '26th', '27th' , '28th' , '29th' , '30th' , '31st'
                     ]

    return 'Today is {} of {} {}'.format(ordinalNumbers[dayNum -1],MONTHS[monthNum -1],weakday)

