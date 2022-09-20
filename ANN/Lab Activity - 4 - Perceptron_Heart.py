#!/usr/bin/env python
# coding: utf-8

# ### Submitted By:
# # Indrashis Paul
# # 19MIM10046

# # Importing required dependencies

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold, GridSearchCV
from sklearn.linear_model import Perceptron


# # Loading data

# In[2]:


data = pd.read_csv('heart-categoric.csv')
print(data.shape)
data.head()


# In[3]:


data.info()


# # Preprocessing
# 1. Label Encoding the Target Column
# 2. Standard scaling the numerical data 

# In[5]:


le = LabelEncoder()

for col in data.columns:
    data[col] = le.fit_transform(data[col])
data.head()


# # Building the Perceptron for Classification

# ## Split data

# In[12]:


X = data.drop('hd', axis=1)
y = data['hd']


# ## Using `sklearn.linear_model.Perceptron`

# ### 1. Default Parameters

# In[7]:


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

# In[8]:


model = Perceptron(penalty='l1', alpha=0.001, max_iter=2000, tol=1e-3, eta0=1.0021, class_weight='balanced', warm_start=True)

# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
# summarize result
print(scores)
print(f'Mean Accuracy: {np.mean(scores)} ({np.std(scores)})')


# In[9]:


model = Perceptron(penalty='l2', alpha=0.00001, max_iter=1000, tol=None, eta0=1.005, class_weight='balanced', warm_start=False)

# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
# summarize result
print(scores)
print(f'Mean Accuracy: {np.mean(scores)} ({np.std(scores)})')


# ### 3. Hyperparameter Tuning

# In[10]:


# define model
model = Perceptron()
# define model evaluation method
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
# define grid
grid = dict()
grid['eta0'] = [0.0001, 0.001, 0.01, 0.1, 1.0]
grid['alpha'] = [0.0001, 0.001, 0.01, 0.1, 1.0]
grid['penalty'] = ['l1', 'l2', 'elasticnet', 'None']
grid['tol'] = [0.0001, 0.001, 0.01, 0.1, 1.0]

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


# ## Using `tf.keras.layers.Dense`

# In[11]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


# In[17]:


model = Sequential()
model.add(Dense(16, input_shape=(4,), activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[18]:


model.summary()


# In[20]:


model.fit(X, y, batch_size=10, epochs=200, verbose=2, validation_split=0.2)


# In[21]:


model.evaluate(X, y)

