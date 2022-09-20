#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing

# In[55]:


# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler


# In[9]:


# Loading the dataset onto a dataframe
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
X


# In[45]:


# Sorting and storing the 2nd column of the dataframe
column_1 = X.iloc[:, 1].sort_values()
column_1


# ## Data Smoothing by Binning

# In[46]:


# Creating empty bins

bin_1 = np.zeros((30, 5))
bin_2 = np.zeros((30, 5))
bin_3 = np.zeros((30, 5))


# In[47]:


# Smoothing by bin mean
def bin_mean(data, bins):
    for i in range(0, 150, 5):
        k = i//5
        mean = data[i:i+5].mean()
        for j in range(5):
            bins[k, j] = mean
    return bins


# In[48]:


bin_1 = bin_mean(column_1, bin_1)
bin_1


# In[49]:


# Smoothing by bin median
def bin_median(data, bins):
    for i in range(0, 150, 5):
        k = i//5
        median = data[i:i+5].median()
        for j in range(5):
            bins[k, j] = median
    return bins


# In[50]:


bin_2 = bin_median(column_1, bin_2)
bin_2


# In[53]:


# Smoothing by bin boundaries
def bin_boundaries(data, bins):
    for i in range(0, 150, 5):
        k = i//5
        for j in range(5):
            if (data[i+j]-data[i]) < (data[i+4]-data[i+j]):
                bins[k, j] = data[i]
            else:
                bins[k, j] = data[i+4]
    return bins


# In[54]:


bin_boundaries(column_1, bin_3)


# ## Data Normalization

# In[58]:


X = data.data
print(X.shape)
X[:5]


# In[60]:


scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)


# In[61]:


print(X_scaled.min(axis=0), X_scaled.max(axis=0))


# In[67]:


def normalize(data):
    X_scaled = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
    return X_scaled


# In[68]:


X_scaled_manual = normalize(X)


# In[71]:


print(X_scaled_manual.min(axis=0), X_scaled_manual.max(axis=0))


# In[70]:


# Verifying Manual vs Sk-Learn
print(np.allclose(X_scaled, X_scaled_manual))

