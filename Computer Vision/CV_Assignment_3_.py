#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/IndraP24/Course-LabWorks/blob/main/Computer%20Vision/CV_Assignment_3_.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow


# In[ ]:


def edgeDetect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    # Here, first argument is the image. Second defines the kernel size.

    #canny
    img_canny = cv2.Canny(img,100,200)

    #sobel
    img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
    img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
    img_sobel = img_sobelx + img_sobely

    #prewitt
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

    print("Canny")
    cv2_imshow(img_canny)
    print("Sobel X")
    cv2_imshow(img_sobelx)
    print("Sobel Y")
    cv2_imshow(img_sobely)
    print("Sobel")
    cv2_imshow(img_sobel)
    print("Prewitt X")
    cv2_imshow(img_prewittx)
    print("Prewitt Y")
    cv2_imshow(img_prewitty)
    print("Prewitt")
    cv2_imshow(img_prewittx+img_prewitty)


# In[ ]:


path_b = '/content/drive/MyDrive/Colab Notebooks/Datasets/Test_Images/I'
for i in range(1,3):
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
    
    edgeDetect(img)
    print("\n\n==============================================\n\n")


# In[ ]:




