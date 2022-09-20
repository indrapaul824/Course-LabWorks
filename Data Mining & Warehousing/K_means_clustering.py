#!/usr/bin/env python
# coding: utf-8

# # Tutorial - 5
# 
# 
# ### Submitted by:
# #### Indrashis Paul - 19MIM10046

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
from sklearn.metrics import silhouette_score


# ## KMeans Clustering

# ### Importing Modules

# ### Data
# 
# Generate the synthetic data and labels

# In[3]:


features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    random_state=42
)


# In[4]:


features[:5]


# In[5]:


true_labels[:5]


# ### Feature Engineering

# In[6]:


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


# In[7]:


scaled_features[:5]


# ### KMeans Clustering

# In[16]:


# Defining the KMeans Class arguments

kmeans_kwargs = {
    "init": "random",
    "n_init": 10,
    "max_iter": 300,
    "random_state": 42,
}


# In[17]:


# Fit the model using Elbow Method

# A list holds the SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)


# ### Evaluation

# In[18]:


# The lowest SSE value
kmeans.inertia_


# In[19]:


# Final locations of the centroid
kmeans.cluster_centers_


# In[20]:


# The number of iterations required to converge
kmeans.n_iter_


# In[21]:


# Checking the labels assigned to 1st 5 points

kmeans.labels_[:5]


# In[23]:


plt.style.use("ggplot")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


# In[24]:


# Choosing optimal number of clusters using Knee Locator

kl = KneeLocator(
    range(1, 11), sse, curve="convex", direction="decreasing"
)

kl.elbow


# ## Agglomerative Clustering

# In[8]:


data = pd.read_csv("./data/Mall_Customers.csv")
print(data.shape)
data.head()


# In[9]:


# Extracting two features
data = data.iloc[:, [3, 4]].values
data[:10]


# ### Determining the optimal number of clusters with dendrogram

# In[13]:


plt.figure(figsize=(15, 7))
dendrogram = sch.dendrogram(sch.linkage(data, method = 'ward')) # finding the optimal number of clusters using dendrogram
plt.title('Dendrogram') # title of the dendrogram
plt.xlabel('Customers') # label of the x-axis
plt.ylabel('Euclidean distances') # label of the y-axis
plt.show() # show the dendrogram


# #### In the dendrogram we have just obtained, the longest vertical line with no extended horizontal line crosses is at the green section. The third line is between euclidian distances (110 - 250). Taking our threshold to be 150, the optimal number of clusters obtained is five.

# ### Agglomerative Clustering model

# In[14]:


Agg_hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = Agg_hc.fit_predict(data) # model fitting on the dataset


# In[17]:


plt.figure(figsize=(15, 7))
# plotting cluster 1
plt.scatter(data[y_hc == 0, 0], data[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1') # plotting cluster 2
plt.scatter(data[y_hc == 1, 0], data[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2') # plotting cluster 3
plt.scatter(data[y_hc == 2, 0], data[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3') # plotting cluster 4
plt.scatter(data[y_hc == 3, 0], data[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')  # plotting cluster 5
plt.scatter(data[y_hc == 4, 0], data[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
# plot title addition
plt.title('Clusters of customers')
# labelling the x-axis
plt.xlabel('Annual Income (k$)')
# label of the y-axis
plt.ylabel('Spending Score (1-100)')
# printing the legend
plt.legend()
# show the plot
plt.show()

