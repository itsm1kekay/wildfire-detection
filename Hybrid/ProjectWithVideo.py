# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:31:01 2025

@author: jojok
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from sklearn.utils import shuffle
import pywt
import os
import time

## Import video ##
## Use CV2 to import parts of flame dataset. ##

vpath = "irflame2.mp4" ##filename (edit as neccessary)
vo = cv2.VideoCapture(vpath)  # Load video
num_frames = 1500
frames = []  # list to store frames
framecount = 0 #counter for loop
new_frames = 0 #counts frames saved by thresholding
wavecount = 0 #counter for wavelet
E = np.zeros(shape=(240,427)) #store temp E for wavelet calc
Eblock = np.zeros(num_frames)
X_train = []  # list to store image features
y_train = []  # list to store labels (fire = 1, no fire = 0)

min_thresh_area = 100  # Adjust as needed

##############################################################################
########## SVM training input ################################################
##############################################################################
start_time1 = time.time()
fire_dir = r"C:\Users\jojok\Desktop\university\EE581\Project\flame1_fire" # Change if necessary
no_fire_dir = r"C:\Users\jojok\Desktop\university\EE581\Project\flame1_nofire"
#These loops takes the images out of the training folers
for i, img_name in enumerate(os.listdir(fire_dir)):
    if i >= 245:  # Stop after 240 images
        break
    img_path = os.path.join(fire_dir, img_name)
    img = cv2.imread(img_path) 
    img = cv2.resize(img, (254, 254))  #resize frame to 254x254
    imgL = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) #convert from BGR to LAB
    
    L_m = np.mean(imgL[:, :, 0])  # lightness
    a_m = np.mean(imgL[:, :, 1])  # green-red
    b_m = np.mean(imgL[:, :, 2])  # blue-yellow

    R1 = imgL[:, :, 0] >= L_m #thresholding rules from paper
    R2 = imgL[:, :, 1] >= a_m
    R3 = imgL[:, :, 2] >= b_m
    R4 = imgL[:, :, 2] >= a_m
        
    train_thresh = R1 & R2 & R3 & R4 #combine masks
        
    masked_frame = np.zeros_like(img)   #make blank zero image

    masked_frame[train_thresh] = img[train_thresh]  #keep thresholded pixels

    masked_frame_rgb = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2RGB) #convert back to rgb
    
    coeffs = pywt.dwt2(masked_frame_rgb[:, :, 0], "haar") #wavelet decomposition
    LL, (LH, HL, HH) = coeffs #keep lh, hl, hh
    
    for k in range(127):
             for l in range(127):
                 E[k][l] = (LH[k][l]**2) + (HL[k][l]**2) + (HH[k][l]**2) #energy per pixel
                 
    Eb_svm = np.sum(E)/16129 #average energy across the frame
    
    X_train.append(Eb_svm) #add to train set
    y_train.append(1)


for i, img_name in enumerate(os.listdir(no_fire_dir)):
     if i >= 245:  # Stop after 240 images
         break
     img_path = os.path.join(no_fire_dir, img_name)
     img = cv2.imread(img_path)
     img = cv2.resize(img, (254, 254))
     imgL = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) #convert from BGR to LAB
     
     L_m = np.mean(imgL[:, :, 0])  # lightness
     a_m = np.mean(imgL[:, :, 1])  # green-red
     b_m = np.mean(imgL[:, :, 2])  # blue-yellow

     R1 = imgL[:, :, 0] >= L_m  #thresholding rules from paper
     R2 = imgL[:, :, 1] >= a_m
     R3 = imgL[:, :, 2] >= b_m
     R4 = imgL[:, :, 2] >= a_m
         
     train_thresh = R1 & R2 & R3 & R4 #combine masks
         
    
     masked_frame = np.zeros_like(img)   #keep thresholded pixels


     masked_frame_rgb = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2RGB) #convert back to rgb
     
     masked_frame[train_thresh] = img[train_thresh] 

     
     coeffs = pywt.dwt2(masked_frame[:, :, 0], "haar") #wavelet decomposition
     LL, (LH, HL, HH) = coeffs  #keep lh, hl, hh
     
     for o in range(127):
              for p in range(127):
                  E[o][p] = (LH[o][p]**2) + (HL[o][p]**2) + (HH[o][p]**2) #energy per pixel
                  
     Eb_svm = np.sum(E)/16129 #average energy across the frame
     
     X_train.append(Eb_svm)  #add to train set
     y_train.append(0)

X_train = np.array(X_train, dtype=np.float32).reshape(-1, 1)  #convert to numpy array
y_train = np.array(y_train, dtype=np.int32)  #convert numpy array
X_train, y_train = shuffle(X_train, y_train, random_state=50) #shuffe training dataset

svm = cv2.ml.SVM_create() #create an SVM class
 
svm.setType(cv2.ml.SVM_C_SVC)  # C-SVM
svm.setKernel(cv2.ml.SVM_LINEAR)  # linear kernel currently
svm.setC(10)  # regularization parameter to try and affect recall
svm.setGamma(0.5)  #gamma

svm.train(X_train, cv2.ml.ROW_SAMPLE, y_train) #train svm
svm.save("svm_model.xml") #save model for reuse

end_time1 = time.time() #used to track time for model
elapsed_time1 = end_time1 - start_time1
print(f"SVM Training Time: {elapsed_time1:.4f} seconds")

##############################################################################
############# VIDEO INPUT ####################################################
##############################################################################
start_time2 = time.time()
start_time3 = time.time() #track model time

if not vo.isOpened(): #input validation for video
     print("Error: Could not open video.")
     exit()

while framecount < (num_frames): #set to control number of frames acquired
     ret, f = vo.read()
    
     f = cv2.resize(f, (854, 480))  #resize frame 
     fL = cv2.cvtColor(f, cv2.COLOR_BGR2LAB) #convert from BGR to LAB
    
     L_m = np.mean(fL[:, :, 0])  # lightness
     a_m = np.mean(fL[:, :, 1])  # green-red
     b_m = np.mean(fL[:, :, 2])  # Blue-Yellow

     R1 = fL[:, :, 0] >= L_m #thresholding rules from paper
     R2 = fL[:, :, 1] >= a_m
     R3 = fL[:, :, 2] >= b_m
     R4 = fL[:, :, 2] >= a_m
    
     fire1thresh = R1 & R2 & R3 & R4 #combine masks
    
     masked_frame = np.zeros_like(f)   #keep thresholded pixels

     masked_frame[fire1thresh] = f[fire1thresh] 
     
     thresh_binary = (fire1thresh * 255).astype(np.uint8)
     contours, _ = cv2.findContours(thresh_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
     for contour in contours: 
        area = cv2.contourArea(contour) #use threshold to make contour
        if area >= min_thresh_area: #if the area bigger than min value
            x, y, w, h = cv2.boundingRect(contour) #diamensions for rounding
            cv2.rectangle(f, (x, y), (x + w, y + h), (0, 0, 0), 2)  # green box
    
     cv2.imshow("Frame with Bounding Boxes", f) #show the images with bounding box
     cv2.waitKey(1)
     
     masked_frame_rgb = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2RGB)
    
     if np.any(fire1thresh):  
         frames.append(masked_frame_rgb)  # add the original frame
         new_frames += 1  # increment counter
    
     framecount += 1  # increment counter
     
end_time3 = time.time()
elapsed_time3 = end_time3 - start_time3
print(f"Video processing time: {elapsed_time3:.4f} seconds")

vo.release()  # release the video file
cv2.destroyAllWindows()  # close openCV windows

while wavecount < new_frames:
     temp_f = frames[wavecount]
     coeffs = pywt.dwt2(temp_f[:, :, 0], "haar") #wavelet decomposition
     LL, (LH, HL, HH) = coeffs #keep detail images
    
     for i in range(240):
         for j in range(427):
             E[i][j] = (LH[i][j]**2) + (HL[i][j]**2) + (HH[i][j]**2) #energy per pixel
    
     Eblock[wavecount] = np.sum(E)/102480 #avg pixel images
    
     wavecount += 1

svm = cv2.ml.SVM_load("svm_model.xml") 
X_test = np.array(Eblock, dtype=np.float32)  # ensure it's float32    

_, predictions = svm.predict(X_test) #save predictions to a list

predictions = predictions.flatten()

end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print(f"Total system processing time: {elapsed_time2:.4f} seconds")

##############################################################################
######################## RESULTS #############################################
##############################################################################

plt.figure(figsize=(10, 5))
plt.plot(Eblock, label="Wavelet Energy")
plt.xlabel("Frame Number")
plt.ylabel("Average Energy")
plt.title("Wavelet Energy Over Time")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(predictions, label="Frame Classification")
plt.xlabel("Frame Number")
plt.ylabel("Classifier")
plt.title("")
plt.legend()
plt.grid()
plt.show()

plt.imshow(masked_frame_rgb)
plt.axis("off")

threshold = 100
true_labels = (Eblock > threshold).astype(int)

accuracy = np.mean(true_labels == predictions) * 100
print(f"Accuracy: {accuracy:.2f}%")

TP = np.sum((predictions == 1) & (true_labels == 1))  # True Positive
FP = np.sum((predictions == 1) & (true_labels == 0))  # False Positive
FN = np.sum((predictions == 0) & (true_labels == 1))  # False Negative
TN = np.sum((predictions == 0) & (true_labels == 0))  # True Negative

print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")
print(f"True Negatives (TN): {TN}")
