# How to run
## Prereq
run on wsl2 and python3.10. Can be dockerized on request
## install packages
run: 
`python3 -m venv ./ee981_group_c`
`source ee981_group_c/bin/activate`
`pip install -r requirements.txt`
## Install datasets
From the [datasets](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs) download the 1.14 gb zenmouse video and place 1-zenmouse vid in the same dir the nb is being run. Additionally download the images and mask datasets (number 9)

Change DS path under preprocessing to images and masks folders and run all
