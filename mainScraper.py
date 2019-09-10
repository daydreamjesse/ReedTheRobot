import getArchives
import update

readme = input("Would you like to read the README? [Y/N]: ")
if readme is "Y":
    # Run this to print the README to the terminal
    file = open("./TextFiles/README.txt", "r")
    print(file.read())
scrapeFrontPage = input("Scrape front page of BZFDNews? [Y/N]: ")
if scrapeFrontPage is "Y":
    print("Getting data from front page...")
    update.getFrontPage()
else:
    print("Cancelled front page scraping.")
scrapeArchive = input("Scrape archives? [Y/N]: ")
if scrapeArchive is "Y":
    getArchives.fetchData()
else:
    print("Cancelled archive scraping.")