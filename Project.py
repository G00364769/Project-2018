
#adarsha sachan
#Project 2018 for Programming and Scripting for Fisher’s Iris data set
import csv
Length = input('Enter Length to find')
Width = input('Enter Width to find')
#def findflowername (number,number2):
 # as line by line 
with open("Data/irish.csv","r") as f:
    reader = csv.reader(f)
    record=""
    for line in reader:
    #for row in line:
      if (line[0] == Length and line[1] == Width):
        #print(line)
        record=line[4]
        print (record)
      elif (line[2] == Length and line[3] == Width):
          record=line[4]
          print (record)
      elif record=="":
         record="there is NoMatch Found"
         print (record)
 