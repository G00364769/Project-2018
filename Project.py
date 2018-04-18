
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

# using Sklern liberary code
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np
#http://docs.python-guide.org/en/latest/scenarios/ml/
#http://scikit-learn.org/stable/user_guide.html
#https://www.python-course.eu/machine_learning_with_scikit.php
#http://scikit-learn.org/stable/tutorial/basic/tutorial.html

#loading the iris dataset
iris = load_iris()

x = iris.data #array of the data
#print(x)
y = iris.target #array of labels of each data entry
#print(y)

#getting label names i.e the three flower species
y_names = iris.target_names
#print(y_names)

#taking random indices to split the dataset into train and test
test_ids = np.random.permutation(len(x))
#test_ids=np.permutation(len(x))
#print(test_ids)

#splitting data and labels into train and test
#keeping last 10 entries for testing, rest for training

x_train = x[test_ids[:-10]]
#print(x_train)
x_test = x[test_ids[-10:]]
#print(x_test)

y_train = y[test_ids[:-10]]
#print(y_train)
y_test = y[test_ids[-10:]]
#print(y_test)

#classifying using decision tree
clf = tree.DecisionTreeClassifier()

#training the classifier with the training set
clf.fit(x_train, y_train)

#predictions for test dataset
pred = clf.predict(x_test)
print (pred )#predicted labels i.e flower species
print (y_test) #actual labels
print (float(accuracy_score(pred, y_test))*100) #prediction accuracy
