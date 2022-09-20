#!/usr/bin/env python
# coding: utf-8

# # Tutorial 2
# 
# Preprocess the attached dataset `food-consumption.csv`. Deal with missing values, transform categorical to numerical form wherever necessary using `LabelEncoder` and `OneHotEncoder`, split the dataset into training set and testing set.

# In[13]:


import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# In[19]:


df = pd.read_csv('./data/food-consumption.csv')
print(df.shape)
df.head()


# In[3]:


df.info()


# ### 1. Null Values

# In[4]:


df.isnull().sum()


# In[7]:


# to interpolate the missing values 
df = df.interpolate(method ='linear', limit_direction ='forward')
df


# In[8]:


# checking for remaining null values
df.isnull().sum()


# ### 2. Encoding the categorical column - `Country`

# #### 1. Using `LabelEncoder`

# In[10]:


le = LabelEncoder()
df['Country_Labelled'] = le.fit_transform(df['Country'])
df['Country_Labelled']


# #### 2. Using `One Hot Encoding` through `pandas.get_dummies()`

# In[18]:


countries = pd.get_dummies(df['Country'])

df = pd.concat([df, countries], axis=1)

df.head()


# ### 3. Splitting the dataset into training and testing sets

# In[17]:


training_set, testing_set = train_test_split(df, test_size=0.2, random_state=42)
print(f"Training Set: {training_set.shape}\nTesting Set: {testing_set.shape}")

