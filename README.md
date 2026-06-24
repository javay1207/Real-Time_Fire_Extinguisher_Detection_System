# Real-Time Fire Extinguisher Detection System 🧯

Real-time fire extinguisher detection system built with YOLOv8 and OpenCV. Replaced traditional classification with advanced deep learning to provide precise bounding box localization. Highly optimized using custom dataset training via Google Colab. Achieves seamless, low-latency live webcam tracking for facility hazard monitoring.

## 🌟 Features

* **High-Precision Object Detection:** Utilizes the cutting-edge YOLOv8 architecture to not only classify but also accurately draw bounding boxes around fire extinguishers in complex environments.
* **Real-Time Inference:** Optimized with `yolov8n` (nano) weights to run smoothly on standard local hardware (e.g., laptop webcams) without severe latency or frame drops.
* **Custom Dataset:** Trained on a meticulously hand-annotated dataset featuring 121 real-world images with diverse lighting, angles, and background clutter to ensure robustness against false positives.

## 🎬 Demonstration

*<video src="[影片網址](https://youtu.be/_UGoffoEEOc?si=6XJvAWaXINltOIFa)" width="100%" controls autoplay loop></video>*

## 📁 Repository Structure

* `detect_yolo_final.py`: The main Python script that initializes the webcam, loads the model, and performs real-time inference using OpenCV.
* `best.pt`: The custom-trained YOLOv8 model weights.
* `requirements.txt`: The list of required Python dependencies to replicate the environment.

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
