<h1 align="center">😺 YOLO cat detection(custom detection) 📷</h1>

<p align="center">
  <i>This project represents my first hands-on exploration of computer vision, following earlier work in NLP.</i>
</p>

## Overview
This project is a <b>custom object detection system</b> built using <b> YOLOv8</b> and a self-labeled dataset to detect my own cats in <b>images, videos, and real-time webcam streams.</b>
The goal was to understand the <b> full computer vision pipeline</b>: data collection, annotation, training, evaluation, and inference.

This project complement my NLP work by demonstrating applied <b>computer vision and deep learning</b>

## 📷 Demo

<p align="center">
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/Screenshots/1.png?raw=true" width="45%" />
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/Screenshots/2.png?raw=true" width="45%" />
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/Screenshots/4.png?raw=true" width="45%" />
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/Screenshots/3.png?raw=true" width="45%" />
</p>
<p align="center"> (Click on the image to see it fully) </p>

<p align="center">
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/Screenshots/webcam.png?raw=true" width="45%" />
</p>
<p align="center"> (This one is from webcam) </p>

---

## Project Highlights
  - Custom dataset annotated in <b>YOLO format</b>
  - Model trained on <b>GPU (RTX 4060 Laptop GPU, CUDA)</b>
  - Real-time <b> Webcam detection</b>
  - Inference <b> CLI and Pyton scripts</b>
  - Training metrics and results visualized


## Dataset
  - <b>Total images:</b> 230
        - Training: ~ 184
        - Validation: 46
  - <b>Classes</b> 
        - `0 - cat`
  - <b>Annotation tool:</b> Label Studio
  - <b> Label format:<b/> YOLO (`class x_center y_center width height`, normalized)


## MODEL & TRAINING
  - <b>Model:</b> YOLOv8n (ULtralytics)
  - <b>Framework</b> Pytorch + Ultralytics YOLO
  - <b>Image Size:</b> 640 x 640
  - <b>Initial training:<b/> 50 epochs
  - <b>Fine-tuning training:<b/> Additional 150 epochs (starting from the best checkpoint
  - <b>Hardware:<b/> NVIDIA RTX 4060 Laptop GPU (CUDA enabled)

## Dataset configuration (cat.yaml)
```
path: ./data
train: images/train
val: images/val

nc: 1
names:
  - cat
```

## Results
  - mAP@0.5: ~0.67
  - mAP@0.5:0.95: ~0.46

<p align="center">
  <img src="https://github.com/Jevinvy/YOLO-cat-detection/blob/main/results.png?raw=true" width="45%" />
</p>
<p align="center"> (Click on the image to see it fully) </p>

Training curves(losses and mAP) are included in `results.png`

Example detections and webcam results are provided in the `Screenshpts/` folder.


---

## Running the Project

### Requirements
```
pip install -r requirements.txt
```
### Webcam Detection (Python)
```
python webcam_cat_detect.py
```
  - Press Q to exit the window

### Image Detection
```
python image_cat_detector.py
```
(Modify the image path inside the script.)

### Video Detection
```
python video_cat_deteect.py
```
Outputs an annotated video file.

### Project Structure
```
YOLO-cat-detection/
├── models/
│   └── best.pt
├── Screenshots/
├── image_cat_detector.py
├── video_cat_detect.py
├── webcam_cat_detect.py
├── cat.yaml
├── requirements.txt
├── results.png
└── README.md

```
---

## What I Learned
  - Increase dataset size and diversity
  - Train with a larger YOLO model (e.g YOLOv8s)
  - Add multi-class detection
  - Build a lightweight web for interface

## Notes
This repository focuses on <b>model training and inference.</b>

### Discalimer ⚠️
This repository is for <b>Educational Purpose Only.</b>



