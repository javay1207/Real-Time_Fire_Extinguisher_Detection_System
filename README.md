# Real-Time Fire Extinguisher Detection System

Real-time fire extinguisher detection system built with YOLOv8 and OpenCV. Replaced traditional classification with advanced deep learning to provide precise bounding box localization. Highly optimized using custom dataset training via Google Colab. Achieves seamless, low-latency live webcam tracking for facility hazard monitoring.
<img width="1418" height="1003" alt="messageImage_1782281960179" src="https://github.com/user-attachments/assets/bbe2b0a2-19d8-4ecd-b183-b932c87c9432" />

## Features

* **High-Precision Object Detection:** Utilizes the cutting-edge YOLOv8 architecture to not only classify but also accurately draw bounding boxes around fire extinguishers in complex environments.
* **Enhanced Model Architecture:** Upgraded to and optimized with `yolov8s` (small) weights to achieve a better balance between higher detection accuracy and real-time performance on local hardware.
* **Custom Dataset:** Trained on a meticulously hand-annotated dataset featuring 121 real-world images with diverse lighting, angles, and background clutter to ensure robustness against false positives.

## Demonstration

[Watch the Demo](https://youtu.be/BpRTH591P2M)

## Repository Structure

* `detect_yolo_final.py`: The main Python script that initializes the webcam, loads the model, and performs real-time inference using OpenCV.
* `best.pt`: The custom-trained YOLOv8s model weights.
* `requirements.txt`: The list of required Python dependencies to replicate the environment.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/javay1207/Real-Time_Fire_Extinguisher_Detection_System.git
   cd Real-Time_Fire_Extinguisher_Detection_System
   ```

2. **(Optional but recommended) Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Inference:**  
Ensure your computer's webcam is connected and accessible. Run the following command in your terminal:
   ```bash
   python detect_yolo_final.py
   ```
   
The system will open a window displaying the live camera feed with detection bounding boxes and confidence scores.


## Training Pipeline
The model was trained entirely on the cloud to bypass local hardware limitations with custom hyperparameter tuning:

* Data Preparation: 121 images were collected and annotated using Roboflow. The dataset was split into Training (70%), Validation (20%), and Testing (10%) sets.

* Model Architecture: YOLOv8 small (yolov8s.pt).

* Hardware & Parameters: Trained via Google Colab (Tesla T4 GPU) using the following custom configuration:

* epochs=40: Extended training duration for better convergence.

* imgsz=800: Increased image resolution to capture finer details of distant fire extinguishers.

* batch=8: Optimized batch processing for the cloud GPU memory.

* **Results:** The model successfully converged, demonstrating exceptional precision and a mean Average Precision (mAP50) approaching 1.0 (nearly 100%) on the validation set, with zero false positives on pure background images.
<img width="2400" height="1200" alt="下載 (1)" src="https://github.com/user-attachments/assets/6a277d66-bc9f-476a-9ff8-22aaf9828e12" />
<img width="1920" height="969" alt="下載 (1)" src="https://github.com/user-attachments/assets/9a3cec63-3573-4061-8164-f66cde698c0b" />


## Practical Applications
This system is designed with real-world smart facility management in mind:

* **Smart Campus Safety Inspection:** Can be integrated into existing CCTV infrastructure to autonomously monitor whether fire safety equipment is present and unobstructed.

* **Emergency Evacuation Assistance:** Serves as a visual aid during emergencies (e.g., smoke or low visibility) to help personnel quickly locate the nearest fire extinguisher.

* **Facility Maintenance Management:** Streamlines routine equipment checks for maintenance staff using mobile devices, replacing manual logs with automated visual verification.
