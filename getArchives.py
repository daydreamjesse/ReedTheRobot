from Webscraping import bzfdscraper as scraper
from DBHandling import dbhandling as db
import checkMemory as mem
import restart
import time
import sys
import os

database = 'bzfdNews'
table = 'archives'

def fetchData():
    confirm = input("Scraping the archives may take awhile. \nAre you sure you want to continue? [Y/N]: ")
    if confirm is "Y":
        db.createTable(database, table)
        date = input("Scraper will retrieve data from beginning of month to end of month two for that year.\n(Separate entries by comma): ")
        dateList = date.split(', ')
        date1 = int(dateList[0])
        date2 = int(dateList[1])
        date3 = int(dateList[2])
        fetchArchives(date1, date2, date3)
    else:
        print("Cancelled scraping.")
    #db.fetchData(database, table)

def insert(archive):
    length = len(archive)
    print("Inserting headlines...")
    start = time.time()
    for i in range(length):
        db.insertData(database, table, archive[i].text.replace('"', ''))
    end = time.time()
    totalTime = end - start
    final = str(round(totalTime, 4))
    print("Successfully inserted archive headlines in " + final + "s.")
def fetchArchives(date1, month1, month2):
    diff = month2 - month1
    year = date1
    if diff == 0:
        archive = scraper.getBzfdArchives(year, month1)
        insert(archive)
    else:
        for j in range(month1, month2+1):
            archive = scraper.getBzfdArchives(year, j)
            insert(archive)