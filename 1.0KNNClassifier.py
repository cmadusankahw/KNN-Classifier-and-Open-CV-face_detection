from sklearn import datasets #importing datasets from sklearn

iris=datasets.load_iris()  #getting the iris dataset

data=iris.data #get data only(features) from iris
target=iris.target #1d array with 150 lables

import numpy as np

train_data= np.delete(data,[0,50,100],axis=0) #axis=0 id given to read by rows,used as this is a 2d array

train_target=np.delete(target,[0,50,100])  #delete 3 lables(targets)

from sklearn.neighbors import KNeighborsClassifier  #Importing ML algorithm to train

clsfr=KNeighborsClassifier()  #Loading the KNN to clasfr(this is the ML box)

clsfr.fit(train_data,train_target) #fit is the command to train the given data using the model

test_data=data[[0,50,100]] #using the original data 2d array

test_target=target[[0,50,100]] #using the original target 1d array

results=clsfr.predict(test_data) #getting results of predictions of the test into results as an array

print("Predicted results : ") 
print(test_data[0]," : " ,results[0])
print(test_data[1]," : " ,results[1])
print(test_data[2]," : " ,results[2],"\n",
      "actual_results :",test_target)
