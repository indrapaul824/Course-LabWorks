#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/IndraP24/Course-LabWorks/blob/main/Computer%20Vision/CV_Assignment_2_.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


import cv2
import numpy
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow


# In[ ]:


def laplace(source):
    source = cv2.GaussianBlur(source,(3,3),0)
    # Here, first argument is the image. Second defines the kernel size.

    # Convert to grayscale:
    source_gray = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)

    # Apply the Laplacian Filter:
    dest = cv2.Laplacian(source_gray,cv2.CV_16S,ksize=3)
    abs_dest = cv2.convertScaleAbs(dest)

    # Showing the output:
    cv2_imshow(abs_dest)


# In[ ]:


path_b = '/content/drive/MyDrive/Colab Notebooks/Datasets/Test_Images/I'
for i in range(1,17):
    path = path_b + str(i)
    if i==1 or i==10:
        path = path + ".png"
    elif i==11:
        path = path + ".tif"
    else:
        path = path + ".jpg"
    img = cv2.imread(path)
    print("Original Image:")
    cv2_imshow(img)
    
    laplace(img)
    print("\n\n==============================================\n\n")

