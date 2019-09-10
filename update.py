from Webscraping import bzfdscraper as scraper
from DBHandling import dbhandling as db

def getFrontPage():
    rawData = scraper.getBzfdHeadlines()
    database = 'bzfdNews'
    table = 'news'
    db.createTable(database, table)
    length = len(rawData)
    headline = []
    for num in range(length):
        headline.append(rawData[num])
    print("Inserting headlines...")
    for i in range(len(headline)):
        db.insertData(database, table, headline[i].replace('"', ''))
    print("Successfully inserted current headlines.")
    #db.fetchData(database, table)
