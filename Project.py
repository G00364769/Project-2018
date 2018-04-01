
#adarsha sachan
#Project 2018 for Programming and Scripting for Fisher’s Iris data set
# Base on sepaland petal length ,width i want to match the record
import csv
SepalLength = input('Enter SepalLength to find')
SepalWidth = input('Enter SepalWidth to find')
PetalLength = input('Enter PetalLength to find')
PetalWidth = input('Enter PetalWidth to find')
#def findflowername (SepalLength,SepalWidth,PetalLength,PetalWidth):
 # as line by line 
with open("Data/irish.csv","r") as f:
    reader = csv.reader(f)
    record=""
    for line in reader:
    #for row in line:
      if (line[0] == SepalLength and line[1] == SepalWidth):
        #print(line)
        record=line[4]
        print (record)
      elif (line[2] == PetalLength and line[3] == PetalWidth):
          record=line[4]
          print (record)
      elif record=="":
         record="there is NoMatch Found"
         print (record)
 