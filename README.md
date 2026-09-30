<div align="center">

# 👁️ VisionGuard

### Real-Time Object Detection using YOLOv8 and OpenCV

A real-time computer vision application that detects objects from a webcam using YOLOv8 and OpenCV.

</div>

---

## 📖 Overview

VisionGuard detects objects from your webcam in real time.

It uses the pretrained **YOLOv8n (Nano)** model from Ultralytics for object detection and **OpenCV** for webcam capture, video processing, and displaying detection results.

The pretrained model can recognize the **80 object classes from the COCO dataset**, including people, phones, laptops, bottles, chairs, and many other common objects.

---

## ✨ Features

- ⚡ Real-time object detection
- 📷 Live webcam integration
- 🔲 Bounding box visualization
- 🏷️ Object name labels with confidence scores
- 🖥️ Console output of detected objects
- 🪶 Lightweight YOLOv8 Nano model
- 💻 Runs on a normal laptop CPU

---

## 🛠️ Tech Stack

| Purpose | Technology |
|---|---|
| Programming Language | Python |
| Object Detection | Ultralytics YOLOv8 |
| Video Processing | OpenCV |
| Detection Model | YOLOv8n |

---

## 📁 Project Structure

```text
Real-Time-Object-Detection-Using-YOLOv8-and-OpenCV/
│
├── main.py          # Webcam capture and detection loop
├── yolov8n.pt       # Pretrained YOLOv8 Nano model
├── .gitignore       # Git ignored files
└── README.md        # Project documentation
