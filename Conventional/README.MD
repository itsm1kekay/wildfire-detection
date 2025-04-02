# Conventional Fire Detection Algorithm - User Guide

## 📌 Overview
This project is a **fire detection algorithm** that processes both video and image datasets to detect potential wildfire occurrences. It utilizes **OpenCV and NumPy** for image processing, color segmentation, motion analysis, and fire classification.

## 🛠️ Requirements
Ensure you have the following dependencies installed:
```bash
pip install opencv-python numpy matplotlib pywavelets
```

## 📂 Dataset Structure
This algorithm is designed to work with the **any** dataset (videos or images), included in the same directory of the notebook. Just copy the path to the dataset's folder/ video file into the `dataset_path` cell. 
For example:
```
dataset_path= "CVSubset/FLAME 3 CV Dataset (Sycan Marsh)/Fire/Thermal/Raw JPG"
```
or 
```
dataset_path= "Videos of Wildfires/Dramatic_evacuations_by_sea_as_forest_fires_rage_in_Italy_and_Turkey.mp4"
```
For video input, please provide a **.mp4, .avi, or .mov** file.

## 🔎 How the Algorithm Works
1. **Preprocessing:** Converts images to HSV, LAB, and grayscale.
2. **Fire Detection:** Uses color segmentation and thresholding in multiple color spaces.
3. **Morphological Filtering:** Refines fire masks using morphological erosion.
4. **Motion Analysis:** Detects flickering using frame differencing.
5. **Contour Detection:** Identifies fire-like regions and filters false positives.
6. **Results:** Outputs detections as video, for an image dataset or plays back the video for a video input and saves bounding box coordinates in `bboxes_output.csv`.

## 📊 Evaluating Performance
_This functionality will be added at a later stage, apologies for the inconvenience!!_
For now you can only view/ playback the output of the algorithm.

## 📄 Output Files
- **fire_detection.mp4** → Processed images with detections.
- **bboxes_output.csv** → Bounding box coordinates for detected fire.

## 📝 Notes
- Adjust HSV/LAB/RGB threshold values if needed to improve detection accuracy.
- False positives can be reduced by tweaking motion filtering parameters.

---
For any issues or improvements, feel free to contribute!