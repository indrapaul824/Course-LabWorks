#!/usr/bin/env python
# coding: utf-8

# # Applying ECL and Perceptron on Data from QP

# ## Error Correction Learning

# ### Importing the Libraries

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# In[9]:


class ECL:

    def __init__(self):
        self.weights=[]

    def activation(self,data):
        #initializing with threshold value
        activation_val=self.weights[0]
        activation_val+=np.dot(self.weights[1:],data)
        return 1 if activation_val>=0 else 0

    def fit(self,X,y,lrate,epochs):
        #initializing weight vector
        self.weights=[0.0 for i in range(len(X.columns)+1)]
        #no.of iterations to train the neural network
        for epoch in range(epochs):
            print(f"Epoch {epoch+1} ...")
            for index in range(len(X)):
                x=X.iloc[index]
                predicted=self.activation(x)
                #check for misclassification
                if(y[index]==predicted):
                    pass
                else:
                    #calculate the error value
                    error=y[index]-predicted
                    #updation of threshold
                    self.weights[0]=self.weights[0]+lrate*error
                    #updation of associated self.weights acccording to Delta rule
                    for j in range(len(x)):
                        self.weights[j+1]=self.weights[j+1]+lrate*error*x[j]
    
    def predict(self,x_test):
        predicted=[]
        for i in range(len(x_test)):
            #prediction for test set using obtained weights
            predicted.append(self.activation(x_test.iloc[i]))
        return predicted
    
    def accuracy(self,predicted,original):
        correct=0
        lent=len(predicted)
        for i in range(lent):
            if(predicted[i]==original[i]):
                correct+=1
        return (correct/lent)*100
    
    def getweights(self):
        return self.weights


# ## Perceptron Learning

# In[10]:


class Perceptron:

    def __init__(self):
        self.weights=[]

    def activation(self,data):
        #initializing with threshold value
        activation_val=self.weights[0]
        activation_val+=np.dot(self.weights[1:],data)
        return 1 if activation_val>=0 else 0

    def fit(self,X,y,lrate,epochs):
        #initializing weight vector
        self.weights=[0.0 for i in range(len(X.columns)+1)]
        #no.of iterations to train the neural network
        for epoch in range(epochs):
            print(f"Epoch {epoch+1} ...")
            for index in range(len(X)):
                x=X.iloc[index]
                predicted=self.activation(x)
                #check for misclassification
                if(y[index]==predicted):
                    pass
                else:
                    #updation of threshold
                    self.weights[0]=self.weights[0]+lrate*y[index]
                    #updation of associated self.weights acccording to Delta rule
                    for j in range(len(x)):
                        self.weights[j+1]=self.weights[j+1]+lrate*x[j]*y[index]
    
    def predict(self,x_test):
        predicted=[]
        for i in range(len(x_test)):
            #prediction for test set using obtained weights
            predicted.append(self.activation(x_test.iloc[i]))
        return predicted
    
    def accuracy(self,predicted,original):
        correct=0
        lent=len(predicted)
        for i in range(lent):
            if(predicted[i]==original[i]):
                correct+=1
        return (correct/lent)*100
    
    def getweights(self):
        return self.weights


# ### Defining Data

# In[3]:


import pandas as pd

X = np.array([[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],  
              [1, 0, 0], 
              [1, 0, 1]], "float32")
y = np.array([[0], 
              [1], 
              [1], 
              [0],
              [0],
              [1]], "float32")
df = pd.DataFrame(X, columns=['a', 'b', 'c'])
y = y.reshape((6,))


# In[11]:


print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size = 0.2, random_state = 0)


# In[12]:


#training the ECL model
model = ECL()
model.fit(X_train, y_train, 0.5, 200)
pred = model.predict(X_test)
print("predicted: ", pred)
print("accuracy: ",model.accuracy(pred, y_test))
print("weights: ",model.getweights())


# In[13]:


#training the percpetron
model = Perceptron()
model.fit(X_train, y_train, 0.5, 200)
pred = model.predict(X_test)
print("predicted: ", pred)
print("accuracy: ",model.accuracy(pred, y_test))
print("weights: ",model.getweights())

