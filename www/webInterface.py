import sys
sys.path.append('../')
from DBHandling import dbhandling as db
#from GPIOTesting import ledflicker as led
import random
from subprocess import call
from num2words import num2words

espeak = "espeak "
devnull = " 2>/dev/null "
save_audio = "--stdout > ./Audio/headline"
wav = ".wav"

def getHeadlines(hid):
    text = db.retrieveData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "*", "episode2final", 1, (hid-1))
    test = (text[0][1])
    #db.deleteData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "generatedHeadlines", ("headline_id = " + str(hid)))
    return test

def speech(text, hid):
    new_string = text.replace("'", "")
    cmd = (espeak + "'" + new_string + "'" + devnull + save_audio + str(hid) + wav)
    #led.flicker(5)
    call([cmd], shell=True)

def getTimeout():
    return(random.randint(120, 180))

