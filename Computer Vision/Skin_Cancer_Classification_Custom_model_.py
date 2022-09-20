#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/IndraP24/Course-LabWorks/blob/main/Computer%20Vision/Skin_Cancer_Classification_Custom_model_.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Skin Cancer Classification
# 
# 

# In[ ]:


get_ipython().system('nvidia-smi')


# # Import Libraries

# In[ ]:


#import the important libraries

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pandas as pd
import datetime
import tensorflow as tf

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, BatchNormalization, Dropout, Dense
from keras.callbacks import ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# The data is obtained from Kaggle. The data loading from Kaggle is shown below.
# 
# There are 7 Classes in that data as follows: 
#  
# 0: Actinic keratoses and intraepithelial carcinoma / Bowen's disease >> `akiec`
#  
# 1: Dermatofibroma >> `df`
# 
# 2: Benign keratosis-like lesions >> `bkl`
# 
# 3: Melanoma >> `mel`
# 
# 4: Melanocytic nevi >> `nv`
# 
# 5: Vascular lesions >> `vasc`
# 
# 6: Basal cell carcinoma >> `bcc`
# 

# # Loading data using Kaggle API

# In[ ]:


# Create a directory called ".kaggle"
get_ipython().system('mkdir ~/.kaggle')


# In[ ]:


# Place the kaggle.json file in the directory
get_ipython().system('cp kaggle.json ~/.kaggle/')


# In[ ]:


# Set permissions of 600 ---> which means that the owner has full read and write access to the file, while no other user can access the file
get_ipython().system('chmod 600 ~/.kaggle/kaggle.json')


# In[ ]:


# Search for the ham10000 dataset in kaggle datasets
get_ipython().system(' kaggle datasets list -s ham10000')


# In[ ]:


# Download the ham10000 dataset
get_ipython().system(' kaggle datasets download -d kmader/skin-cancer-mnist-ham10000')


# In[ ]:


# Unzip images and place them in a directory
get_ipython().system('mkdir skin-cancer-mnist-ham10000')
get_ipython().system('unzip /content/skin-cancer-mnist-ham10000.zip -d skin-cancer-mnist-ham10000')


# # Reading a specific csv file

# In[ ]:


df = pd.read_csv('../content/skin-cancer-mnist-ham10000/hmnist_28_28_RGB.csv')
df = df.sample(frac = 1) # randomize the data
data = df.iloc[:,:-1] # extract the pixel data
labels = df.iloc[:,-1:] # extract the corresponding labels
df.head()


# In[ ]:


labels.head(30)


# # Data distribution

# In[ ]:


type_of_cancer = ['akiec','df','bkl','mel','nv','vasc','bcc']
counts = list(labels.value_counts())
plt.figure(figsize = (8,6))
ax = sns.countplot(x='label', data=df)
ax.set_xticklabels(type_of_cancer)


# The data is heavily imbalanced which leads to a significant effect on the values of metrics

# We do the following for resolving the problem:
# 
# 1. We duplicated the other classes "randomly " other than `nv` class (Data Duplication)
# 
# 
# 2. Generate new images with 'ImageDataGenarator' from Keras (Data Augmentation)

# In[ ]:


df = df.sort_values('label') # Sorting the data according to the labels
df = df.reset_index()


# In[ ]:


df


# # Data Duplication
# 
# Here we duplicate the class of the data for some amount of times.
# 
# The 4th index is ignored as it is the imbalanced class.

# In[ ]:


index0 = df[df['label'] == 0].index.values
index1 = df[df['label'] == 1].index.values
index2 = df[df['label'] == 2].index.values
index3 = df[df['label'] == 3].index.values
index5 = df[df['label'] == 5].index.values
index6 = df[df['label'] == 6].index.values


# In[ ]:



df0 = df.iloc[int(min(index0)):int(max(index0)+1)]
df1 = df.iloc[int(min(index1)):int(max(index1)+1)]
df2 = df.iloc[int(min(index2)):int(max(index2)+1)]
df3 = df.iloc[int(min(index3)):int(max(index3)+1)]
df5 = df.iloc[int(min(index5)):int(max(index5)+1)]
df6 = df.iloc[int(min(index6)):int(max(index6)+1)]


# We have taken some random optimal values to centralize the new data which contains the duplicated data along with the previous data.

# In[ ]:



df_index0 = df0.append([df0]*17, ignore_index = True)
df_index1 = df1.append([df1]*15, ignore_index = True)
df_index2 = df2.append([df2]*5, ignore_index = True)
df_index3 = df3.append([df3]*52, ignore_index = True)
df_index5 = df5.append([df5]*45, ignore_index = True)
df_index6 = df6.append([df6]*5, ignore_index = True)

frames = [df, df_index0, df_index1, df_index2, df_index3, df_index5, df_index6]


# In[ ]:


# Concatenating all the feature dataframes to form the final dataframe
final_df = pd.concat(frames)
final_df.drop('index', inplace = True, axis = 1)
final_df = final_df.sample(frac = 1)
data = final_df.iloc[:,:-1]
labels = final_df.iloc[:,-1:]


# ### We can now see that The Distribution of The  classes are more Normalized and More Balanced

# In[ ]:


type_of_cancer = ['akiec','df','bkl','mel','nv','vasc','bcc']
counts = list(labels.value_counts())
plt.figure(figsize = (8,6))
ax = sns.countplot(x='label', data=df)
ax.set_xticklabels(type_of_cancer)


# # Image data preprocessing

# Now we can divide the data. 
# 
# X : feature "for the data "
# 
# Y : labels "for the lables"
# 
# 
# 
# 

# In[ ]:


X = np.array(data)
Y = np.array(labels)


# ## Reshaping the data

# In[ ]:



X = X.reshape(-1,28,28,3)

print( X.shape)
print( Y.shape)


# ## Normalizing the data 

# In[ ]:


X = (X-np.mean(X))/np.std(X)


# ## Splitting the data into train and the test data

# In[ ]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

print( X_train.shape)
print( X_test.shape)
print( Y_train.shape)
print( Y_test.shape)


# # Data Augmentation with ImageDataGenerator

# In[ ]:



train_datagen = ImageDataGenerator(rescale = 1./255,
                                  rotation_range = 10,
                                  width_shift_range = 0.2,
                                  height_shift_range = 0.2,
                                  shear_range = 0.2,
                                  horizontal_flip = True,
                                  vertical_flip = True,
                                  fill_mode = 'nearest')
train_datagen.fit(X_train)

test_datagen = ImageDataGenerator(rescale = 1./255)
test_datagen.fit(X_test)

train_data = train_datagen.flow(X_train, Y_train, batch_size = 64)
test_data = test_datagen.flow(X_test, Y_test, batch_size = 64)


# # Modeling

# ## Model architecture

# In[ ]:


model = Sequential([
    
    Conv2D(16, kernel_size = (3,3), input_shape = (28, 28, 3), activation = 'relu', padding = 'same'),
    Conv2D(32, kernel_size = (3,3), activation = 'relu'),
    MaxPool2D(pool_size = (2,2)),

    Conv2D(32, kernel_size = (3,3), activation = 'relu', padding = 'same'),
    Conv2D(64, kernel_size = (3,3), activation = 'relu'),
    MaxPool2D(pool_size = (2,2), padding = 'same'),

    Conv2D(64, kernel_size = (3,3), activation = 'relu'),
    Conv2D(64, kernel_size = (3,3), activation = 'relu', padding = 'same'),
    MaxPool2D(pool_size = (2,2), padding = 'same'),

    Flatten(),
    
    Dense(64, activation = 'relu'),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(32, activation='relu'),
    Dense(7, activation='softmax')]
)


# ### Adjusting learning rate and the optimizer 

# In[ ]:



learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy', 
                                            patience=3, 
                                            verbose=1, 
                                            factor=0.5, 
                                            min_lr=0.00001)

optimizer = tf.keras.optimizers.Adam(learning_rate = 0.00075,
                                    beta_1 = 0.9,
                                    beta_2 = 0.999,
                                    epsilon = 1e-8)


# In[ ]:



model.compile(optimizer = optimizer,
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])


# In[ ]:


model.summary()


# In[ ]:


from keras.utils.vis_utils import plot_model
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)


# ## Fitting the model

# In[ ]:


epochs = 20

history = model.fit(X_train,
                    Y_train,
                    validation_split=0.2,
                    batch_size = 64,
                    epochs = epochs,
                    callbacks=[learning_rate_reduction]) 


# # Model Evaluation on test data

# In[ ]:


model_acc_test = model.evaluate(X_test, Y_test, verbose=0)[1]
print("the test model accuracy =",model_acc_test * 100)


# # Model Performance measures

# In[ ]:


ACC = history.history['accuracy']
VAL_ACC = history.history['val_accuracy']

plt.figure(figsize=(8,6))
plt.title("the accuracy of the training and validation phase of the model")
plt.plot(ACC, label = 'train_acc')
plt.plot(VAL_ACC, label = 'val_acc')
plt.legend()


# In[ ]:


LOSS = history.history['loss']
VAL_LOSS = history.history['val_loss']

plt.figure(figsize=(8,6))
plt.title("the loss of the training and validation phase of the model")
plt.plot(LOSS, label = 'train_loss')
plt.plot(VAL_LOSS, label = 'val_loss')
plt.legend()


# ## Confusion Matrix

# In[ ]:



Y_true = np.array(Y_test)

Y_pred = model.predict(X_test)
Y_pred = np.array(list(map(lambda x: np.argmax(x), Y_pred)))

cm1 = confusion_matrix(Y_true, Y_pred)
plt.figure(figsize=(12, 6))
plt.title('the confusion matrix of the model in the train')
sns.heatmap(cm1, annot = True, fmt = 'g' ,vmin = 0, cmap = 'binary')


# # Classification report
# 
# - precision
# 
# - recall
# 
# - f1-score
# 
# - accuracy

# In[ ]:


label_mapping = {
    0: 'nv',
    1: 'mel',
    2: 'bkl',
    3: 'bcc',
    4: 'akiec',
    5: 'vasc',
    6: 'df'
}

classification_report_model = classification_report(Y_true, Y_pred, target_names=label_mapping.values())
print(classification_report_model)


# # Saving the model for further use

# In[ ]:


model.save('my_model.h5')

