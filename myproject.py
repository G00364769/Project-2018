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
    if sepalWidth < 5:
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
Perimeter=(sepallength+sepalWidth)+(Petallength+PetallWidth)
Perimeter=2*Perimeter
#totalarea=format(totalarea,'.2f')
print(petalarea,Perimeter)
#if petal area less then 2 and total area less than 16 its Setosa
 #condition 1
if petalarea < 2.00 and Perimeter < 25.00:
  #print("this is Iris-Setos ")
  Flo="Iris-setosa"
  print("Based on my analysis this is",Flo)
  #condition 2 
elif (Perimeter < 33.00) and (petalarea < 7.00) :
  #print("this is ris- virginica ")
  Flo="Iris-versicolor"
  print("Based on my analysis this is",Flo)
  #condition 3
else:
  Flo="Iris-virginica"
  print("Based on my analysis this is",Flo)
# creat colum for each row ,
creat_coloum =['sepallength' , 'sepalWidth' , 'prtallength' , 'prtalwidth' , 'Flowername','PetalArea', 'PerimeterArea']
# adding header and cloum
read=pd.read_table('Data/irish.csv',sep=',',header=None,names=creat_coloum)
readmean=read.groupby('Flowername').mean()
read['PetalArea']=read['prtallength']*read['prtalwidth']
read['PerimeterArea']=2*(read['prtallength']+read['prtalwidth']+read['sepallength']+read['sepalWidth'])
#print(read['PetalArea'])
print(read['PerimeterArea'])
# creating mean bar pannel
test=read.groupby('Flowername').mean().plot(kind='bar')
graph.show()
# reading each flower index
Flower=read['Flowername']
sepalX=read['sepallength']
sepalY=read['sepalWidth']
PetalX=read['prtallength']
PetalY=read['prtalwidth']
# base on flower name for Sepal providing graph as well my record but thay are diff mark
X=graph.scatter(Flower,sepalX,color=['b'])
y=graph.scatter(Flower,sepalY,color=['c'])
# my input record sepal
X=graph.scatter(Flo,sepallength,color=['r'],s=34,marker="*")
y=graph.scatter(Flo,sepalWidth,color=['m'],s=34,marker="*")
# x and y cordinate added lable
graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF FLOWER')
# added title
graph.title('For Sepal record in Scatter ')
# in grf show legend
graph.legend()
graph.show()
# base on flower name for Petal providing graph as well my record but thay are diff mark
t=graph.scatter(Flower,PetalX,color=['r'])
s=graph.scatter(Flower,PetalY,color=['m'])
# my input record for petal
X=graph.scatter(Flo,Petallength,color=['b'],s=34,marker="*")
y=graph.scatter(Flo,PetallWidth,color=['c'],s=34,marker="*")
graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF FLOWER')
graph.title('For Petal record in Scatter ')
graph.legend()
graph.show()
# both record sepal and Petal as well my record but thay are diff mark
t=graph.scatter(Flower,sepalY)
t=graph.scatter(Flower,sepalX)
t=graph.scatter(Flower,PetalY)
t=graph.scatter(Flower,PetalX)

X=graph.scatter(Flo,Petallength,color=['b'],s=234,marker="o")
y=graph.scatter(Flo,PetallWidth,color=['c'],s=234,marker="8")
X=graph.scatter(Flo,sepallength,color=['r'],s=234,marker="8")
y=graph.scatter(Flo,sepalWidth,color=['m'],s=234,marker="o")

graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF FLOWER')
graph.title('For ALL record in Scatter ')
graph.legend()
graph.show()
# my logic graph Scatter
t=graph.scatter(Flower,read['PerimeterArea'])
t=graph.scatter(Flower,read['PetalArea'])
graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF FLOWER')
graph.title('For based on My logic  Scatter ')
graph.legend()
graph.show()