#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/IndraP24/Course-LabWorks/blob/main/ANN/Lab%20Activity%20-%207%20-%20ANN_Class_Activity.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Import libraries

# In[ ]:


import pandas as pd
import numpy as np


# # Read data

# In[ ]:


df1 = pd.read_csv('myFile0.csv')
df2 = pd.read_csv('myFile1.csv')
print(df1.shape, df2.shape)


# In[ ]:


df1.head()


# In[ ]:


df2.head()


# # Convert `DataFrame` to numpy `array`

# In[ ]:


m1 = df1.values
m2 = df2.values
print(m1.shape, m2.shape)


# In[ ]:


m1


# In[ ]:


m2


# In[ ]:


m3 = m2.T
print(m3.shape)
m3


# # Matrix Operations

# ### Matrix Addition

# In[ ]:


def matadd(m1: np.ndarray, m2: np.ndarray):
    """Adds two matrix after checking possibility."""
    if m1.shape == m2.shape:
        return m1+m2
    else:
        return "Addition not possible because of inconsistent shape"


# In[ ]:


matadd(m1, m2)


# In[ ]:


matadd(m1, m3)


# ### Matrix Multiplication

# In[ ]:


def matmul(m1: np.ndarray, m2: np.ndarray):
    """Multiplies two matrix after checking possibility."""
    if m1.shape[0] == m2.shape[1]:
        return m1 @ m2
    else:
        return "Multiplication not possible because of inconsistent shape"


# In[ ]:


matmul(m1, m3)


# In[ ]:


matmul(m1, m2)

