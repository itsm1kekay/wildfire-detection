# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:18:48 2025

@author: jojok
"""

import skimage as ski
import numpy as np
import pywt

from skimage import io, color
import matplotlib.pyplot as plt

image1 = io.imread("fire1.jpg") 
image2 = io.imread("fire2.jpg") 
image3 = io.imread("fire3.jpg") 

image4 = io.imread("nofire1.jpg") 
image5 = io.imread("nofire1.jpg") 
image6 = io.imread("nofire1.jpg") 

fire1lab = color.rgb2lab(image1)

L_m = np.mean(fire1lab[:, :, 0])  # Lightness
a_m = np.mean(fire1lab[:, :, 1])  # Green-Red
b_m = np.mean(fire1lab[:, :, 2])  # Blue-Yellow

R1 = fire1lab[:, :, 0] >= L_m
R2 = fire1lab[:, :, 1] >= a_m
R3 = fire1lab[:, :, 2] >= b_m
R4 = fire1lab[:, :, 2] >= a_m

fire1thresh = R1 & R2 & R3 & R4

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Original Image
axes[0].imshow(image1)
axes[0].set_title("Original Image")
axes[0].axis("off")

# Thresholded Binary Mask
axes[1].imshow(fire1thresh, cmap="gray")
axes[1].set_title("Thresholded Mask")
axes[1].axis("off")

#Wavelet Analysis
coeffs1 = pywt.dwt2(image1[:, :, 0], "haar")
LL1, (LH1, HL1, HH1) = coeffs1

coeffs2 = pywt.dwt2(image4[:, :, 0], "haar")
LL2, (LH2, HL2, HH2) = coeffs2

E1 = np.zeros(shape=(127,127))
E2 = np.zeros(shape=(127,127))

for i in range(127):
    for j in range(127):
        E1[i][j] = (LH1[i][j]**2) + (HL1[i][j]**2) + (HH1[i][j]**2)

for p in range(127):
    for k in range(127):
        E2[p][k] = (LH2[p][k]**2) + (HL2[p][k]**2) + (HH2[p][k]**2)
        
E1block = np.sum(E1)/127
E2block = np.sum(E2)/127

# nofire1lab = color.rgb2lab(image4)
# L_m = np.mean(nofire1lab[:, :, 0])  # Lightness
# a_m = np.mean(nofire1lab[:, :, 1])  # Green-Red
# b_m = np.mean(nofire1lab[:, :, 2])  # Blue-Yellow

# R1 = nofire1lab[:, :, 0] >= L_m
# R2 = nofire1lab[:, :, 1] >= a_m
# R3 = nofire1lab[:, :, 2] >= b_m
# R4 = nofire1lab[:, :, 2] >= a_m

# nofire1thresh = R1 & R2 & R3 & R4

# fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# # Original Image
# axes[0].imshow(image4)
# axes[0].set_title("Original Image")
# axes[0].axis("off")

# # Thresholded Binary Mask
# axes[1].imshow(nofire1thresh, cmap="gray")
# axes[1].set_title("Thresholded Mask")
# axes[1].axis("off")
