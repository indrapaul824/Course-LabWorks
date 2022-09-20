#!/usr/bin/env python
# coding: utf-8

# # OR Gate Output prediction using predefined Network from Paper

# ## Imports

# In[18]:


import numpy as np


# ## Creating the data

# ### Regular OR Data

# In[19]:


Xr = np.array([[0, 0],
               [0, 1], 
               [1, 0], 
               [1, 1]], "float32")
yr = np.array([[0], 
               [1], 
               [1], 
               [1]], "float32")


# ### Bipolar OR Data

# In[20]:


Xb = np.array([[1, 1],
               [1, -1], 
               [-1, 1], 
               [-1, -1]], "float32")
yb = np.array([[1], 
               [0], 
               [0], 
               [-1]], "float32")


# ## Building provided model

# In[9]:


def threshold(x):
    if x>0:
        return 1
    elif x == 0:
        return 0
    return -1

def trained_nn(x, y):
    w3 = [0.4, -0.7]
    w4 = [0.6, -0.5]
    b3 = -0.3
    b4 = 0.4
    w5 = [2.0, 1.0]
    b5 = 0.0
    yhat = []
    
    for xi in x:
        yhat.append(threshold(xi@w3+b3 + xi@w4+b4 + b5))
    
    return yhat

def accuracy(y, yhat):
    res = []
    if len(y) == len(yhat):
        for i in range(len(y)):
            if y[i] == yhat[i]:
                res.append(True)
            else:
                res.append(False)
    
    return res


# ### Testing Regular Data

# In[21]:


yhat = trained_nn(Xr, yr)
res = accuracy(yr, yhat)
print("Accuracy:", res)


# ### Testing Bipolar Data

# In[22]:


yhat = trained_nn(Xb, yb)
res = accuracy(yb, yhat)
print("Accuracy:", res)

