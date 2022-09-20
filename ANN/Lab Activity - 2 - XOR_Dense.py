#!/usr/bin/env python
# coding: utf-8

# # Understanding XOR gate characteristics with Neural Networks

# ## Imports

# In[1]:


import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ## Creating the data

# In[2]:


X = np.array([[0, 0],
              [0, 1], 
              [1, 0], 
              [1, 1]], "float32")
y = np.array([[0], 
              [1], 
              [1], 
              [0]], "float32")


# ## Building, training and evaluating the model

# ### Creating a custom Callback to stop when accuracy reaches 100

# In[32]:


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        thres = 1.0
        if(logs.get('accuracy') >= thres): # Experiment with changing this value
            print(f"\nReached {thres*100}% accuracy on epoch = {epoch+1}!")
            self.model.stop_training = True


# ### Model 1 -> Dense1: 16, epochs: 200

# In[40]:


callback = myCallback()
model = Sequential([
    Dense(16, input_dim=2, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='mean_squared_error', 
              optimizer='adam',
              metrics=['accuracy'])


# In[41]:


model.fit(X, y, epochs=200, callbacks=[callback], verbose=2)


# In[42]:


print(model.predict(X).round())


# ### Model 2 -> Dense1: 64, epochs: 100

# In[44]:


callback = myCallback()
model = Sequential([
    Dense(64, input_dim=2, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(loss='mean_squared_error', 
              optimizer='adam',
              metrics=['accuracy'])


# In[45]:


model.fit(X, y, epochs=100, callbacks=[callback], verbose=2)


# In[46]:


print(model.predict(X).round())

