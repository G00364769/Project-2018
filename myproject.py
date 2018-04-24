# adarsha sachan
# i have build my own algorithm that will tell me flower name
# and its with dataset set analysis
import pandas as pd
import matplotlib.pyplot as graph
# Write a  true condition 
while True:
  try:
    # input condition for sepallength
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
     # input condition for sepalWidth
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
    # input condition for Petallength
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
    ## input condition for PetallWidth
    PetallWidth=float( input ("Please Enter the PetallWidth "))
    if PetallWidth < 3:
     # print ("success")
      break
    else: 
      print ("PetallWidth should be less than 3 Cm")
  except ValueError:
    print ("Not a Number")
#using area formula get petalarea
petalarea= (Petallength*PetallWidth)
#petalarea=format(petalarea,'.2f')
sepalarea=(sepallength*sepalWidth)
#sepalarea=format(sepalarea,'.2f')
Perimeter=(sepallength+sepalWidth)+(Petallength+PetallWidth)
Perimeter=2*Perimeter
#totalarea=format(totalarea,'.2f')
#print(petalarea,Perimeter)
#if petal area less then 2 and total area less than 16 its Setosa
 #condition 1
if petalarea < 2.00 and Perimeter < 25.00:
  #print("this is Iris-Setos ")
  Flo="Iris-setosa"
  print("Based on my analysis this is",Flo)
   #condition 3 as per user story
elif (Perimeter < 33.00) and (petalarea  > 7.65) and (petalarea  < 9.00)  :
  #print("this is ris- virginica ")
  Flo=" 80% Iris-virginica and 20% Iris-versicolor "
  print("Based on my analysis this is",Flo)
 #condition 2 as per user story
elif (Perimeter < 33.00) and (petalarea < 9.00) :
  #print("this is ris- virginica ")
  Flo="Iris-versicolor"
  print("Based on my analysis this is",Flo)
  #condition 4 as per user story
else:
  Flo="Iris-virginica"
  print("Based on my analysis this is",Flo)
# creat colum for each row ,PetalArea,PerimeterArea
creat_coloum =['sepallength' , 'sepalWidth' , 'petallength' , 'petalwidth' , 'Flowername','PetalArea', 'PerimeterArea']#,'SepalArea']
# adding header and cloum
read=pd.read_table('Data/irish.csv',sep=',',header=None,names=creat_coloum)
#print(read)
readmean=read.groupby('Flowername').mean()
#print(readmean)
# create entry for sepal ,petal,perimeter area
read['PetalArea']=read['petallength']*read['petalwidth']
#read['SepalArea']=read['sepallength']*read['sepalWidth']
read['PerimeterArea']=2*(read['petallength']+read['petalwidth']+read['sepallength']+read['sepalWidth'])
#print(read['PetalArea'])
#print(read['PerimeterArea'])
# creating mean bar pannel
BAR=read.groupby('Flowername').mean().plot(kind='bar')
mean=BAR=read.groupby('Flowername').mean()
#print(mean)
graph.show()
# reading each flower record index
Flower=read['Flowername']
sepalX=read['sepallength']
sepalY=read['sepalWidth']
PetalX=read['petallength']
PetalY=read['petalwidth']
# based on flower name [X cordinate] for Sepal length and width creating scatter graph
X=graph.scatter(Flower,sepalX,color=['b'])
y=graph.scatter(Flower,sepalY,color=['c'])
# Representing my input record in sepal VS identified flower
X=graph.scatter(Flo,sepallength,color=['r'],s=34,marker="*")
y=graph.scatter(Flo,sepalWidth,color=['m'],s=34,marker="*")
# x and y cordinate added lable
graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF sepallength and sepalwidth')
# added title
graph.title('Input records are highlighting for sepallength and sepalwidth ')
# in grf show legend
graph.legend()
graph.show()
## based on flower name [X cordinate] for Petal length and width creating scatter graph
t=graph.scatter(Flower,PetalX,color=['r'])
s=graph.scatter(Flower,PetalY,color=['m'])
# Representing my input record in Petal VS identified flower
X=graph.scatter(Flo,Petallength,color=['b'],s=34,marker="*")
y=graph.scatter(Flo,PetallWidth,color=['c'],s=34,marker="*")
graph.xlabel('Xcoordinate OF FLOWER')
graph.ylabel('Ycoordinate OF Petal length and Petal width')
graph.title('Input records are highlighting for Petallength and Petalwidth ')
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
# my logic graph in Scatter form
t=graph.scatter(Flower,read['PerimeterArea'])
t=graph.scatter(Flower,read['PetalArea'])
#t=graph.scatter(Flower,read['SepalArea'])
graph.xlabel('Xcoordinate of FLOWER Record')
graph.ylabel('Ycoordinate of PerimeterArea and PetalArea')
graph.title('Scatter graph based on PerimeterArea and PetalArea ')
graph.legend()
graph.show()

print("Second method using sklearn running program   ")
#http://docs.python-guide.org/en/latest/scenarios/ml/
#http://scikit-learn.org/stable/user_guide.html
#https://www.python-course.eu/machine_learning_with_scikit.php
#http://scikit-learn.org/stable/tutorial/basic/tutorial.html
#http://www.pythonforbeginners.com/os/pythons-os-module
import os
#https://docs.python.org/3/library/pickle.html
import pickle
#http://scikit-learn.org/stable/tutorial/basic/tutorial.html#machine-learning-the-problem-setting
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
#http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
from sklearn.tree import DecisionTreeRegressor
#loading the iris dataset
iris = load_iris()
x = iris.data #array of the data
#print("Full Record in array",x)
y = iris.target #array of labels of each data entry as flower name
#print("labels of each data entry",y)
#getting label names the three flower species
y_names = iris.target_names
#print("Flower name",y_names)
#taking random indices to split the dataset into train and test
test_ids = np.random.permutation(len(x))
#test_ids=np.permutation(len(x))
#print(test_ids)
#splitting data and labels into train and test
#keeping last 10 entries for testing, rest for training
TrainData = x[test_ids[:-60]]
#print(TrainData)
#InputTrainData = x[test_ids[-10:]]
#print(InputTrainData)
TrainFlower = y[test_ids[:-60]]
#print(TrainFlower)
y_test = y[test_ids[-60:]]
#print(y_test)
#print(y_test)
#classifying using decision tree
clf = tree.DecisionTreeClassifier()
#training the classifier with the training set
clf.fit(TrainData, TrainFlower)
InputTrainData = x[test_ids[-60:]]
#InputTrainData = [[sepallength,sepalWidth,Petallength,PetallWidth]]
#predictions for test dataset
pred = clf.predict(InputTrainData)
#print ("pred", pred )#predicted labels i.e flower species
accuracy= (float(accuracy_score(pred, y_test))*100) #prediction accuracy
print("prediction percentage",accuracy)
# using DecisionTreeRegressor mim and max value
tree = DecisionTreeRegressor(max_depth=60, random_state=0).fit(TrainData , TrainFlower)
#model_dir = "\model"
# this will creat path in destop
Path = os.path.dirname(os.getcwd())
#print (Path)
#SAV is a file extension used for the saved date of SPSS (Statistical Package for the Social Sciences).
filename = Path + '\\finalized_model.sav'
print("Creating model path in destop",filename)
# Save a dictionary into a pickle file.
pickle.dump(tree, open(filename, 'wb'))
## save the model to disk
filename =  Path + '\\finalized_model.sav'
# providing user input record in model
print("Checking input record In build in model") 
## load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
#predicted = loaded_model.predict([a,b,c,d].reshape(1, -1))
#pridicted as per input record
predicted= loaded_model.predict([[sepallength,sepalWidth,Petallength,PetallWidth]])
graph.hist(predicted)
graph.show()
print("predicted value form model set",predicted)
if predicted == 0:
  print("prediction percentage is",accuracy,"Iris-setosa")
elif predicted == 1:
  print("prediction percentage is",accuracy,"Iris-versicolor")
elif predicted ==2:
  print("prediction percentage is",accuracy,"Iris-virginica")