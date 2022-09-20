#!/usr/bin/env python
# coding: utf-8

# ### Submitted By:
# # Indrashis Paul
# # 19MIM10046

# # Importing required dependencies

# In[43]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold, GridSearchCV
from sklearn.linear_model import Perceptron
import torch
import torch.nn as nn
import torchmetrics


# # Loading data

# In[44]:


data = pd.read_csv('gender.csv')
print(data.shape)
data.head()


# In[45]:


data.info()


# # Preprocessing
# 1. Label Encoding the Target Column
# 2. Standard scaling the numerical data 

# In[46]:


le = LabelEncoder()

data['gender'] = le.fit_transform(data['gender'])
data.head()


# In[47]:


scaler = MinMaxScaler()

std_col = ['forehead_width_cm','forehead_height_cm']
data[std_col] = scaler.fit_transform(data[std_col])
data.head()


# # Building the Perceptron for Classification

# ## Split data

# In[48]:


X = data.drop('gender', axis=1)
y = data['gender']


# ## Using `sklearn.linear_model.Perceptron`

# ### 1. Default Parameters

# In[49]:


# define model
model = Perceptron()

# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
# summarize result
print(scores)
print(f'Mean Accuracy: {np.mean(scores)} ({np.std(scores)})')


# ### 2. Custom Parameters

# In[50]:


model = Perceptron(penalty='l1', alpha=0.001, max_iter=2000, tol=1e-3, eta0=1.0021, class_weight='balanced', warm_start=True)

# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
# summarize result
print(scores)
print(f'Mean Accuracy: {np.mean(scores)} ({np.std(scores)})')


# In[51]:


model = Perceptron(penalty='l2', alpha=0.00001, max_iter=1000, tol=None, eta0=1.005, class_weight='balanced', warm_start=False)

# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
# summarize result
print(scores)
print(f'Mean Accuracy: {np.mean(scores)} ({np.std(scores)})')


# ### 3. Hyperparameter Tuning

# In[52]:


# define model
model = Perceptron()
# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# define grid
grid = dict()
grid['eta0'] = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0]
grid['alpha'] = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0]
grid['penalty'] = ['l1', 'l2', 'elasticnet', 'None']
grid['tol'] = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0]
grid['validation_fraction'] = [0.1, 0.15, 0.2, 0.25, 0.3]

# define search
search = GridSearchCV(model, grid, scoring='accuracy', cv=cv, n_jobs=-1)
# perform the search
results = search.fit(X, y)
# summarize
print('Best Mean Accuracy: %.3f' % results.best_score_)
print('Best Config: %s' % results.best_params_)
# summarize all
means = results.cv_results_['mean_test_score']
params = results.cv_results_['params']
for mean, param in zip(means, params):
    print(">%.3f with: %r" % (mean, param))


# ## Using `torch.nn.Sequential`

# In[54]:


# build the model
Perceptron = nn.Sequential(
    nn.Linear(7,1),   # input layer
    nn.Sigmoid()
  )

Perceptron


# In[55]:


X = X.values
y = y.values
y = y.reshape((y.shape[0], 1))


# In[56]:


X = torch.tensor(X).float()
y = torch.tensor(y).float()

print(X.shape)
print(y.shape)


# In[57]:


# other model features
learningRate = .03

# loss function
lossfun = nn.BCELoss()

# optimizer
optimizer = torch.optim.Adam(Perceptron.parameters(),lr=learningRate)


# In[58]:


# train the model
numepochs = 1000
losses = torch.zeros(numepochs)

for epochi in range(numepochs):

  # forward pass
  yHat = Perceptron(X)

  # compute loss
  loss = lossfun(yHat, y)
  losses[epochi] = loss

  # backprop
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()


# In[59]:


# show the losses

plt.plot(losses.detach(),'o',markerfacecolor='w',linewidth=.1)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()


# In[60]:


Perceptron.eval()
y_pred = Perceptron(X)

acc = torchmetrics.functional.accuracy(y_pred.int(), y.int())
acc


# ## Using `tf.keras.layers.Dense`

# In[4]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


# In[2]:


data = pd.read_csv('gender.csv')
print(data.shape)
data.head()


# In[3]:


le = LabelEncoder()

data['gender'] = le.fit_transform(data['gender'])
data


# In[6]:


sc = MinMaxScaler()

num = ['forehead_width_cm', 'forehead_height_cm']
data[num] = sc.fit_transform(data[num])
data


# In[15]:


X = data.iloc[:, :data.shape[1]-1].values
y = data.iloc[:, data.shape[1]-1:].values


# In[19]:


model = Sequential()
model.add(Dense(1, input_shape=(7,), activation='relu'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[20]:


model.summary()


# In[23]:


model.fit(X, y, batch_size=25, epochs=75, verbose=2, validation_split=0.2)


# In[24]:


model.evaluate(X, y)


# In[ ]:




