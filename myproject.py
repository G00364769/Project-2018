# adarsha sachan
# i have build my algorithm that will tell whatsa flower name
# and its without traing set
import pandas as pd
import matplotlib.pyplot as graph
while True:
  try:
    sepallength=float( input ("Please Enter the sepallength "))
    if sepallength < 8:
      #print ("success")
      break
    else: 
      print ("sepallength should be less than 8 Cm")
  except ValueError:
    print ("Not a Number")

while True:
  try:
    sepalWidth=float( input ("Please Enter the sepalWidth "))
    if sepalWidth < 4:
     # print ("success")
      break
    else: 
      print ("sepalWidth should be less than 4 Cm")
  except ValueError:
   print ("Not a Number")

while True:
  try:
    Petallength=float( input ("Please Enter the Petallength "))
    if Petallength <7:
      #print ("success")
      break
    else: 
      print ("Petallength should be less than 7 Cm")
  except ValueError:
    print ("Not a Number")

while True:
  try:
    PetallWidth=float( input ("Please Enter the PetallWidth "))
    if PetallWidth < 3:
     # print ("success")
      break
    else: 
      print ("PetallWidth should be less than 3 Cm")
  except ValueError:
    print ("Not a Number")

petalarea= (Petallength*PetallWidth)
#petalarea=format(petalarea,'.2f')
sepalarea=(sepallength*sepalWidth)
#sepalarea=format(sepalarea,'.2f')
totalarea=(sepallength*sepalWidth)*(Petallength*PetallWidth)
#totalarea=format(totalarea,'.2f')
print(petalarea,sepalarea,totalarea)
#if petal area less then 2 and total area less than 16 its Setosa
 #condition 1
if petalarea < 2.00 and totalarea < 17.00:
  print("this is Iris-Setos ")
  #condition 2 
elif (totalarea > 172.00) and (petalarea > 10.10) :
  print("this is ris- virginica ")
  #condition 3
elif (totalarea < 172.00) and (petalarea < 7.60) :
  print("this is Iris- versicolor flower")
  #condition 4
elif (totalarea < 172.00) and (petalarea > 7.60) and (sepalarea > 18.40):
  print("this is Iris- versicolor flower")
  #condition 5
elif (totalarea < 172.00) and (petalarea > 7.60) and (sepalarea > 16.00 and sepalarea <= 17.00 ):
  print("this is Iris- versicolor flower")
  #condition 6
else:
  print("this is ris- virginica ")

creat_coloum =['sepallength' , 'sepalWidth' , 'prtallength' , 'prtalwidth' , 'Flowername' ]
read=pd.read_table('Data/irish.csv',sep=',',header=None,names=creat_coloum)
read=read.groupby('Flowername').mean()
read=read.groupby('Flowername').mean().plot.bar()
graph.show()