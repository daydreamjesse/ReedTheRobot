from textgenrnn import textgenrnn as tg
import string
from tqdm import tqdm
import sys
sys.path.append('../')
from DBHandling import dbhandling as db

textgen = tg         (weights_path='test3_weights.hdf5',
                     vocab_path='test3_vocab.json',
                     config_path='test3_config.json')

#textgen.generate_samples(max_gen_length=1000)

def returnXSamples(x):
       samples = []
       for i in tqdm(range(x)):
              samples.append(returnSample())
       return samples
       
def returnSample():
       sample = textgen.generate(1, return_as_list=True)[0]
       if len(sample) > 1:
              newSample = sample.replace(" ' re", "'re")
              aSample = newSample.replace("' s", "")
              newSample2 = aSample.replace(" ' s", "'s")
              newSample3 = newSample2.replace(" ' ll", "'ll")
              newSample4 = newSample3.replace(" , ", ", ")
              finalSample = string.capwords(newSample4)
              return finalSample

def reedToDB():
       while True:
           num = input("How many samples do you want Reed to store?: ")
           if num == "0":
                  break
           else:
                  pass
           textArr = returnXSamples(int(num))
           for i in range(len(textArr)):
               print(textArr[i])
               text = textArr[i].replace('"', '')
               db.insertData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "generatedHeadlines", "headline", text)
    
def terminalGenerate():
       while True:
              gen = input("Generate headline? [Y/N]: ")
              if gen == "Y":
                     sample = returnSample()
                     print(sample)
                     insert = input("Insert into database? [Y/N]: ")
                     if insert == "Y":
                            text = sample.replace('"', '')
                            db.insertData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "episode2", "headline", text)
                     else:
                            continue
              else:
                     sys.exit()

def testToProduction():
       count = 0
       db.createTable("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "episode2final", ["id", "headline"], ["INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT", "TEXT NOT NULL"])
       while True:
              sample = db.retrieveData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "*", "episode2", 1, count)
              text = sample[0][1]
              print(text)
              keep = input("Would you like to keep this for the episode? (to terminate enter '0') [Y/N]: ")
              if keep == "Y":
                     edit = input("Would you like to make any edits? [Y/N]: ")
                     if edit == "Y":
                            finalText = input("Enter edited headline: ")
                     else:
                            finalText = text
                     db.insertData("/home/pi/Desktop/ReedTheRobot/Databases/reedHeadlines", "episode2final", "headline", finalText)
                     count += 1
                     print("Inserted into final table.")
              elif keep == "0":
                     sys.exit()
              else:
                     count += 1
                     print("Moving to next entry...")
                     continue

testToProduction()
#terminalGenerate()
