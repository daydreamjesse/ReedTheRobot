import sqlite3
from subprocess import run

def dbCreate(db):
    try:
        connection = sqlite3.connect('{}.db'.format(db))
        return connection
    except:
        print("Error occured, killing process.")
        
if __name__ == '__main__':
    db = input("Enter name of database: ")
    dbCreate(db)