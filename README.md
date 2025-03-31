<table style="width: 100%; table-layout: fixed ">
  <tr>
    <td>
      <img src="/assets/Logo.png" width = "200">
    </td>
    <td style="text-align: center">
      <h2>Real-time Wildfire Detection</h2>
      <p>Wildfires are a serious global threat, making early detection essential. This project compares conventional image processing techniques with an ML-driven approach to detect wildfires in real-time.</p>
    </td>
  </tr>
</table>


## Description
Repository for group project in real-time wildfire detection for the EE581 module at the University of Strathclyde, developed by Group 8 (Joseph Kromer, Sai Tam, Mukul Narwani and Michail Kasmeridis). 
The project is split into 3 parts, each person developing an algorithm, capable of detecting wildfires in real-time.
  - The first algorithm developed by Michail Kasmeridis uses conventional image processing techniques and can be found [here](https://github.com/itsm1kekay/wildfire-detection/conventional).
  - The second algorithm, developed by Joseph Kromer, used conventional + ML to develop a hybrid model and can be found [here](https://github.com/itsm1kekay/wildfire-detection/hybrid).   
  - The third algorithm, developed by Mukul Narwani, is a Convolutional Neural Network based off of UNet and can be found [here](https://github.com/itsm1kekay/wildfire-detection/UNet).
  - The fourth algorithm, developed by Sai Tam, is another Convolutional Neural Network based off of YOLO and can be found [here](https://github.com/itsm1kekay/wildfire-detection/YOLO).
  - The 4 approaches (conventional, ML and hybrid) will be evaluated using the metrics shown in [Performance](https://github.com/itsm1kekay/wildfire-detection/edit/main/README.md#performance).

The current progress of the group is tracked using a [Gannt Chart](https://github.com/itsm1kekay/wildfire-detection/edit/main/README.md#gantt-chart).

## Flow charts and system design
### Conventional approach:
<h1 align="center">
  <img src= "/assets/Conventional Approach.png"
  width = "400"
</h1>

### Hybrid approach:
<h1 align="center">
  <img src= "/assets/Hybrid Approach.png"
  width = "400"
</h1>

### ML approach:
<h1 align="center">
  <img src= "/assets/DL pipeline.png"
  width = "400"
</h1>

## Performance
|      Metrics       |Conventional|  Yolo  |  U-Net  |   Hybrid   |
|--------------------|------------|--------|---------|------------|
|Computational cost  |    Small   |   TBD  |   Very high (12GB VRAM)   |    Medium     |
|Speed (in fps)      |  ~55    |   TBD  |   ~45   |    TBD     |
|Precision           |    N/A     |   TBD  |   0.84- 0.96   |    1     |
|Recall              |    N/A     |   TBD  |   0.60-0.68   |    0.56     |

## Gantt Chart
<h1 align="center">
  <img src= "/assets/EE581 Gantt Chart.png"
  width = "1000"
</h1>
  
## Websites for images 
- https://www.goes.noaa.gov
- https://terra.nasa.gov/about/terra-instruments/modis 
- https://data-nifc.opendata.arcgis.com/search?tags=cy_wildlandfire_opendata%2CCategory
- https://ieee-dataport.org/open-access/flame-3-radiometric-thermal-uav-imagery-wildfire-management
- https://ieee-dataport.org/open-access/flame-2-fire-detection-and-modeling-aerial-multi-spectral-image-dataset
- https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs

  
## References
<a id="1">[1]</a> 
A. Shamsoshoara, F. Afghah, A. Razi, L. Zheng, P. Z. Fulé, and E. Blasch, “Papers with Code - FLAME Dataset,” Paperswithcode.com, Dec. 28, 2020. https://paperswithcode.com/dataset/flame (accessed Dec. 08, 2024).

<a id="2">[2]</a> 
I. El-Madafri, M. Peña, and N. Olmedo-Torre, “The Wildfire Dataset: Enhancing Deep Learning-Based Forest Fire Detection with a Diverse Evolving Open-Source Dataset Focused on Data Representativeness and a Novel Multi-Task Learning Approach,” Forests, vol. 14, no. 9, p. 1697, Sep. 2023, [![DOI:10.3390/f14091697](https://zenodo.org/badge/DOI/10.3390/f14091697.svg)](https://doi.org/10.3390/f14091697)

<a id="3">[3]</a> 
“Wildfire Prediction Dataset (Satellite Images)”,  https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset (accessed Dec. 08, 2024).

<a id="4">[4]</a> 
A. Rafiee, Reza Dianat, M. Jamshidi, R. Tavakoli, and S. Abbaspour, “Fire and smoke detection using wavelet analysis and disorder characteristics,” Mar. 2011, 
[![DOI:10.1109/iccrd.2011.5764295](https://zenodo.org/badge/DOI/10.1109/iccrd.2011.5764295.svg)](https://doi.org/10.1109/iccrd.2011.5764295)

<a id="5">[5]</a> 
Z. Zhang, J. Zhao, D. Zhang, C. Qu, Y. Ke, and B. Cai, “Contour Based Forest Fire Detection Using FFT and Wavelet,” Jan. 2008, 
[![DOI:10.1109/csse.2008.837](https://zenodo.org/badge/DOI/10.1109/csse.2008.837.svg)](https://doi.org/10.1109/csse.2008.837)

<a id="6">[6]</a> 
S. Verstockt, I. Kypraios, P. De Potter, C. Poppe, and R. Van de Walle, “Wavelet-based multi-modal fire detection,” IEEE Xplore, Apr. 2015, Accessed: Dec. 06, 2024. [Online]. Available: https://ieeexplore.ieee.org/abstract/document/7074248

<a id="7">[7]</a> 
Z. Jiao, Y. Zhang, J. Xin, Y. Yi, D. Liu, and H. Liu, “Forest Fire Detection with Color Features and Wavelet Analysis Based on Aerial Imagery,” Nov. 2018, 
[![DOI:10.1109/cac.2018.8623473](https://zenodo.org/badge/DOI/10.1109/cac.2018.8623473.svg)](https://doi.org/10.1109/cac.2018.8623473)

<a id="8">[8]</a> 
T. Celik, “Fast and Efficient Method for Fire Detection Using Image Processing,” ETRI Journal, vol. 32, no. 6, pp. 881–890, Dec. 2010, 
[![DOI:10.4218/etrij.10.0109.0695](https://zenodo.org/badge/DOI/10.4218/etrij.10.0109.0695.svg)](https://doi.org/10.4218/etrij.10.0109.0695)

<a id="9">[9]</a> 
P. Zhang, Y. Ban, and A. Nascetti, “Learning U-Net without forgetting for near real-time wildfire monitoring by the fusion of SAR and optical time series,” Remote Sensing of Environment, vol. 261, p. 112467, Aug. 2021, 
[![DOI:10.1016/j.rse.2021.112467](https://zenodo.org/badge/DOI/10.1016/j.rse.2021.112467.svg)](https://doi.org/10.1016/j.rse.2021.112467)

<a id="10">[10]</a> 
L. Qiao, Y. Zhang, and Y. Qu, “Pre-processing for UAV Based Wildfire Detection: A Loss U-net Enhanced GAN for Image Restoration,” Oct. 2020, [![DOI:10.1109/iai50351.2020.9262172](https://zenodo.org/badge/DOI/10.1109/iai50351.2020.9262172.svg)](https://doi.org/10.1109/iai50351.2020.9262172)

<a id="11">[11]</a> 
Rahmi Arda Aral, Cemil Zalluhoğlu, and Ebru Akçapınar Sezer, “Lightweight and attention-based CNN architecture for wildfire detection using UAV vision data,” International Journal of Remote Sensing, vol. 44, no. 18, pp. 5768–5787, Sep. 2023, [![DOI:10.1080/01431161.2023.2255349](https://zenodo.org/badge/DOI/10.1080/01431161.2023.2255349.svg)](https://doi.org/10.1080/01431161.2023.2255349)

<a id="12">[12]</a> 
P. V. A. B. de Venâncio, A. C. Lisboa, and A. V. Barbosa, “An automatic fire detection system based on deep convolutional neural networks for low-power, resource-constrained devices,” Neural Computing and Applications, vol. 34, no. 18, pp. 15349–15368, Jun. 2022, [![DOI:10.1007/s00521-022-07467-z](https://zenodo.org/badge/DOI/10.1007/s00521-022-07467-z.svg)](https://doi.org/10.1007/s00521-022-07467-z)

<a id="13">[13]</a> 
A. Mohapatra and T. Trinh, “Early Wildfire Detection Technologies in Practice—A Review,” Sustainability, vol. 14, no. 19, p. 12270, Sep. 2022, [![DOI:10.3390/su141912270](https://zenodo.org/badge/DOI/10.3390/su141912270.svg)](https://doi.org/10.3390/su141912270)

<a id="14">[14]</a> 
A. Bouguettaya, H. Zarzour, A. M. Taberkit, and A. Kechida, “A review on early wildfire detection from unmanned aerial vehicles using deep learning-based computer vision algorithms,” Signal Processing, vol. 190, no. 108309, Jan. 2022,
[![DOI:10.1016/j.sigpro.2021.108309](https://zenodo.org/badge/DOI/10.1016/j.sigpro.2021.108309.svg)](https://doi.org/10.1016/j.sigpro.2021.108309)

<a id="15">[15]</a> 
Z. Jiao et al., “A Deep Learning Based Forest Fire Detection Approach Using UAV and YOLOv3,” IEEE Xplore, pp. 1–5, Jul. 2019, [![DOI:10.1109/ICIAI.2019.8850815](https://zenodo.org/badge/DOI/10.1109/ICIAI.2019.8850815.svg)](https://doi.org/10.1109/ICIAI.2019.8850815)

<a id="16">[16]</a> 
M. Li et al., “A Real-time Fire Segmentation Method Based on A Deep Learning Approach,” IFAC-PapersOnLine, vol. 55, no. 6, pp. 145–150, 2022, [![DOI:10.1016/j.ifacol.2022.07.120](https://zenodo.org/badge/DOI/10.1016/j.ifacol.2022.07.120.svg)](https://doi.org/10.1016/j.ifacol.2022.07.120)

<a id="17">[17]</a> 
P. Barmpoutis, T. Stathaki, K. Dimitropoulos, and N. Grammalidis, “Early Fire Detection Based on Aerial 360-Degree Sensors, Deep Convolution Neural Networks and Exploitation of Fire Dynamic Textures,” Remote Sensing, vol. 12, no. 19, p. 3177, Sep. 2020, [![DOI:10.3390/rs12193177](https://zenodo.org/badge/DOI/10.3390/rs12193177.svg)](https://doi.org/10.3390/rs12193177)

<a id="18">[18]</a> 
M. A. I. Mahmoud and H. Ren, “Forest Fire Detection and Identification Using Image Processing and SVM,” Journal of Information Processing Systems, vol. 15, no. 1, pp. 159–168, 2019, [![DOI:10.3745/JIPS.01.0038](https://zenodo.org/badge/DOI/10.3745/JIPS.01.0038.svg)](https://doi.org/10.3745/JIPS.01.0038)

<a id="19">[19]</a> 
J. Gubbi, S. Marusic, and M. Palaniswami, “Smoke detection in video using wavelets and support vector machines,” Fire Safety Journal, vol. 44, no. 8, pp. 1110–1115, Nov. 2009, [![DOI:10.1016/j.firesaf.2009.08.003](https://zenodo.org/badge/DOI/10.1016/j.firesaf.2009.08.003.svg)](https://doi.org/10.1016/j.firesaf.2009.08.003)

<a id="20">[20]</a> 
H. Harkat, H. F. T. Ahmed, J. M. P. Nascimento, and A. Bernardino, “Early fire detection using wavelet based features,” Measurement, vol. 242, p. 115881, Jan. 2025, [![DOI:10.1016/j.measurement.2024.115881](https://zenodo.org/badge/DOI/10.1016/j.measurement.2024.115881.svg)](https://doi.org/10.1016/j.measurement.2024.115881)

<a id="21">[21]</a> 
L. Huang, G. Liu, Y. Wang, H. Yuan, and T. Chen, “Fire detection in video surveillances using convolutional neural networks and wavelet transform,” Engineering Applications of Artificial Intelligence, vol. 110, p. 104737, Apr. 2022, 
[![DOI:10.1016/j.engappai.2022.104737](https://zenodo.org/badge/DOI/10.1016/j.engappai.2022.104737.svg)](https://doi.org/10.1016/j.engappai.2022.104737)
