#!/usr/bin/env python
# coding: utf-8

# # DMDW-Tutorial-4-C11+C12-slot

# ### Submitted By:
# ### Indrashis Paul - 19MIM10046

# In[ ]:


# Installing the required packages
# %pip install mlxtend


# ## Step 1: Importing libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


# ## Step 2 : Data Pre-processing 

# In[4]:


# Importing the dataset
# we will ignore the headers as our csv files contains the records from first row itself
df = pd.read_csv('./data/store_data.csv',header=None)
print(df.shape)
df.head()


# In[5]:


# now we need to convirt this data into proper format that cam be fed to Apriori Algorithm. 
# columns should represent unique items and rows must represent transactions. True will represent that item is the part of that transaction.


# In[6]:


final_data = pd.DataFrame(columns=['Transaction','Items'])
df = df.T
for col in df.columns:
    col_data = list(df[col].dropna())
    temp_dict = {'Transaction':[int(col)]*len(col_data),  'Items':col_data }
    temp_df = pd.DataFrame(temp_dict)
    final_data = final_data.append(temp_df,ignore_index=True)
final_data.head()


# In[16]:


final_data_dummy = pd.get_dummies(final_data['Items'])
final_data_dummy['Transaction'] = final_data['Transaction']
# i don't want the quantity, I want just that product is bought or #not(after doing dummy yow will get 2 if same item bought twice in a #transaction) so i will use encode_units function
def encode_units(x):
    if x <=  0:
        return 0
    if x >=  1:
        return 1
format_data= final_data_dummy.groupby('Transaction').sum()
format_data = format_data.applymap(encode_units)
format_data.head()


# ##### Above data is in the required format

# ## Step 3 : EDA

# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
order = final_data['Items'].value_counts()[:10].index
sns.countplot(x = 'Items',data=final_data,order = order)
plt.title('Top 10 most selling items')
plt.show()


# In[15]:


# unique items and total number of transactions
len(final_data['Items'].unique())
len(final_data['Transaction'].unique())


# ## Step 4: Modelling

# In[20]:


frequent_itemsets  =  apriori(format_data, min_support = 0.01, use_colnames = True)
frequent_itemsets.head()


# In[22]:


# No lets apply association rules


# In[23]:


result = association_rules(frequent_itemsets, metric = "lift", min_threshold=0.01)
result.sort_values('lift',ascending=False)


# <center>----------End---------</center>
