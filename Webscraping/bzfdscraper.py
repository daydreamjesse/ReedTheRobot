from bs4 import BeautifulSoup
from tqdm import tqdm
import pycld2 as translator
import time
import requests

bzfd = requests.get('https://www.buzzfeednews.com') #GET request for connecting to buzzfeed
newsTitles = [] # list of headlines
archiveTitles = [] # list of archived headlines

def getBzfdHeadlines():
    soup = BeautifulSoup(bzfd.text, 'html.parser')
    # get all the headlines from the front page of Buzzfeed
    start = time.time()
    for title in tqdm(soup.select('.newsblock-story-card__title')):
        #strip any whitespace at the beginning and end and convert to str
        newsTitles.append(title.get_text().strip())
    end = time.time()
    final = end - start
    totalTime = str(round(final, 4))
    print("Successfully scraped BZFD headlines in " + totalTime + "s.")
    return newsTitles

def testing():
    for i in tqdm(range(9, 13)):
        for j in range(1, 32):
            try:
                archive = requests.get('https://www.buzzfeed.com/archive/2012/' + str(i) + '/' + str(j))
                soup = BeautifulSoup(archive.text, 'html.parser')
                for title in soup.findAll('a', attrs={'class' : 'js-card__link link-gray'}):
                    if title is not None:
                            archiveTitles.append(title)
            except:
                continue
    

def getBzfdArchives(date, mon):
    url = ("https://www.buzzfeed.com/archive/" + str(date) + "/" + str(mon))
    timeString = []
    if mon is 1:
        month = "Scraping January..."
    elif mon is 2:
        month = "Scraping February..."
    elif mon is 3:
        month = "Scraping March..."
    elif mon is 4:
        month = "Scraping April..."
    elif mon is 5:
        month = "Scraping May..."
    elif mon is 6:
        month = "Scraping June..."
    elif mon is 7:
        month = "Scraping July..."
    elif mon is 8:
        month = "Scraping August..."
    elif mon is 9:
        month = "Scraping September..."
    elif mon is 10:
        month = "Scraping October..."
    elif mon is 11:
        month = "Scraping November..."
    elif mon is 12:
        month = "Scraping December..."
    for i in range(1, 32):
        dateString = ("/" + str(i))
        timeString.append(dateString)
    print("Collecting data from year " + str(date) + "...")
    start = time.time()
    print(month)
    for i in tqdm(range(31)):
        try:
            archive = requests.get(url+timeString[i])
            soup = BeautifulSoup(archive.text, 'html.parser')
            for title in soup.findAll('a', attrs={'class' : 'js-card__link link-gray'}):
                if title is not None:
                    archiveTitles.append(title)
        except:
            print("The URL either does not exist or does not allow robots.")
    end = time.time()
    final = end - start
    totalTime = round(final, 4)
    print("Successfully scraped BZFD Archives for " + str(date) + "/" + str(mon) + " in " + str(totalTime) + "s.")
    return archiveTitles