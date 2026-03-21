# The Predator-Prey Encounter Detection (PrED) Model
The python scripts and requirements needed to run the Predator-Prey Encounter Detection Model

## Intended use
The Predator-Prey Encounter Detection Model is intended to be used to detect encounters between a semi-sessile rotifer species, *Philodina* sp., and a motile algal species, *Cryptomonas erosa*. This model requires Ultralytics YOLOv5 to run as well as the dependencies listed in the 'requirements.txt' file. 

In addition to detecting and classifying, this model as the added functions of estimating algal density and generating a 'potential encounter' log in the form of a csv file. The potential encounter log includes the range of frame numbers, the range of timestamps, and the unique identifiers involved in a potential encounter. The algal density estimate will be printed in the terminal once the 'pred_detect_sort.py' script finishes. The log will be saved in the parent directory.

## Steps

### 1. Clone the YOLOv5 Repository

Clone the Ultralytics YOLOv5 repository. It can be found here (https://github.com/ultralytics/yolov5)

### 2. Clone the PrED-Model repository

### 3. Copy the files from this repository into the cloned YOLOv5 repository
    1. Copy the scripts ('*.py') and the 'requirements.txt' file and paste them directly into the YOLOv5 parent folder
    2. Move the 'weights' folder into the YOLOv5 parent folder
    3. Copy the 'bdelloids.yaml' file from the 'PrED-Model/data' folder and paste it into the 'YOLOv5/data' folder.
    
### 4. In the terminal, change the working directory to the YOLOv5 parent folder
`cd ./yolov5`

### 5. Install Requirements
**You may want to create a virutal environment using something like 'conda' before attempting this step.**
`pip install -r requirements.txt`

### 6. Run 'pred_detect_sort.py' Script
To run the PrED model, run the following command in your terminal

`python pred_detect_sort.py --imgsz 1920 --weights ./weights/best.pt --source <location of video file>  --conf 0.1`

  Additional arguments added in for PrED:
  
      `volume_arena` (float): The volume of water seen in the video in mm^3. Default is 0.00482
      `volume_total` (float): The total volume of water mm^3. Default is 1000

### Outputs
The outputs of the script are:

      1. A potential encounter log titled '{video name}_frame_ranges.csv'
      2. An estimate of algal density printed in the terminal
      3. An annotated video with class and 'Encounter!' bounding boxes. This will be saved in 'yolov5/runs/exp[number]'.



