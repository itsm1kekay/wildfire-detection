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
The project is split into 2 parts - two subgroups - developing an algorithm each, capable of detecting wildfires in real-time.
  - The first group, comprising of Joseph Kromer and Michail Kasmeridis, are developing an algorithm that uses conventional image processing techniques to identify wildfires.
  - The second group, comprising of Sai Tam and Mukul Narwani, are developing a Machine Learning algorithm that classifies wildfires.
  - In subsequent times, the groubs will unite and collaborate in a hybrid approach. [[1]](#1)
  - The 3 approaches (conventional, ML and hybrid) will be evaluated using the metrics shown in [Performance](https://github.com/itsm1kekay/wildfire-detection/edit/main/README.md#performance).

The current progress of the group is tracked using a [Gannt Chart](https://github.com/itsm1kekay/wildfire-detection/edit/main/README.md#gantt-chart).

## Flow charts and system design
### Conventional approach:
<h1 align="center">
  <img src= "/assets/Conventional Approach.jpg"
  width = "400"
</h1>

### ML approach:
<h1 align="center">
  <img src= "/assets/DL pipeline.png"
  width = "400"
</h1>

## Performance
|      Metrics       |Convensional|  ML-model  |   Hybrid   |
|--------------------|------------|------------|------------|
|Computational cost  |    TBD     |    TBD     |    TBD     |
|Speed (in fps)      |    TBD     |    TBD     |    TBD     |
|Adaptability        |    TBD     |    TBD     |    TBD     |
|Detection rate      |    TBD     |    TBD     |    TBD     |
|False positives     |    TBD     |    TBD     |    TBD     |
|False negatives     |    TBD     |    TBD     |    TBD     |

## Gantt Chart
<h1 align="center">
  <img src= "/assets/EE581 Gantt Chart.png"
  width = "1000"
</h1>
  
## Links given for wildfire-detection
- https://www.goes.noaa.gov
- https://terra.nasa.gov/about/terra-instruments/modis 
- https://data-nifc.opendata.arcgis.com/search?tags=cy_wildlandfire_opendata%2CCategory 
- https://github.com/DeepCube-org/uc3-public-notebooks/blob/main/1_UC3_Datacube_Access_and_Plotting.ipynb
  
## References
<a id="1">[1]</a> 
A. Rafiee, Reza Dianat, M. Jamshidi, R. Tavakoli, and S. Abbaspour, “Fire and smoke detection using wavelet analysis and disorder characteristics,” Mar. 2011, 
[![DOI:10.1109/iccrd.2011.5764295](https://zenodo.org/badge/DOI/10.1109/iccrd.2011.5764295.svg)](https://doi.org/10.1109/iccrd.2011.5764295)

<a id="2">[2]</a> 
Z. Zhang, J. Zhao, D. Zhang, C. Qu, Y. Ke, and B. Cai, “Contour Based Forest Fire Detection Using FFT and Wavelet,” Jan. 2008, 
[![DOI:10.1109/csse.2008.837](https://zenodo.org/badge/DOI/10.1109/csse.2008.837.svg)](https://doi.org/10.1109/csse.2008.837)

<a id="3">[3]</a> 
S. Verstockt, I. Kypraios, P. De Potter, C. Poppe, and R. Van de Walle, “Wavelet-based multi-modal fire detection,” IEEE Xplore, Apr. 2015, Accessed: Dec. 06, 2024. [Online]. Available: https://ieeexplore.ieee.org/abstract/document/7074248

<a id="4">[4]</a> 
Z. Jiao, Y. Zhang, J. Xin, Y. Yi, D. Liu, and H. Liu, “Forest Fire Detection with Color Features and Wavelet Analysis Based on Aerial Imagery,” Nov. 2018, 
[![DOI:10.1109/cac.2018.8623473](https://zenodo.org/badge/DOI/10.1109/cac.2018.8623473.svg)](https://doi.org/10.1109/cac.2018.8623473)

<a id="5">[5]</a> 
T. Celik, “Fast and Efficient Method for Fire Detection Using Image Processing,” ETRI Journal, vol. 32, no. 6, pp. 881–890, Dec. 2010, 
[![DOI:10.4218/etrij.10.0109.0695](https://zenodo.org/badge/DOI/10.4218/etrij.10.0109.0695.svg)](https://doi.org/10.4218/etrij.10.0109.0695)

<a id="6">[6]</a> 
I. Bosch, A. Serrano, and L. Vergara, “Multisensor Network System for Wildfire Detection Using Infrared Image Processing,” The Scientific World Journal, vol. 2013, no. 1, pp. 1–10, Jan. 2013, [![DOI:10.1155/2013/402196](https://zenodo.org/badge/DOI/10.1155/2013/402196.svg)](https://doi.org/10.1155/2013/402196)
