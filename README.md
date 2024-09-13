

# Osiris Detection

**Osiris Detection** is a Kivy-based application designed for real-time object detection using a YOLO model. This tool is aimed at detecting hazardous objects in manufacturing environments. The application provides a user-friendly interface and leverages computer vision to identify and track objects with high confidence.

## Features

- **Real-time Object Detection:** Utilizes the YOLO model to detect objects in video streams.
- **User Interface:** Provides a clear and simple interface for interaction.
- **Live Feedback:** Displays detection results and confidence levels in real-time.

## Requirements

- **Python 3.x**
- **Kivy**
- **OpenCV**
- **Ultralytics YOLO** (for object detection)
- **file location :** /Users/mehdiamrani/carew dental/grenade project/model-2.pt

## Installation

To set up the environment for running this application, follow these steps:

1. **Install the required Python packages:**

   ```bash
   pip install kivy opencv-python-headless ultralytics
   ```

2. **Download or prepare the YOLO model file (`model-2.pt`):**
   - Ensure you have the `model-2.pt` file for YOLO model inference. This file should be located in the same directory as the script.

## Usage

1. **Run the application:**

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python file.

2. **Interface Overview:**

   - **InterfaceScreen:** The main screen where you can start the detection process by clicking the "Test the AI Model" button.
   - **DetectionScreen:** The screen that shows the video feed from the camera along with detection results. It displays detected objects, their confidence levels, and counts.

3. **Detection Logic:**

   - The application captures video frames from the camera.
   - The YOLO model processes each frame to detect objects.
   - Detected objects with a confidence score of 0.5 or higher are highlighted.
   - The results, including the detected object's label and confidence, are displayed in real-time.

## Code Description

- **`InterfaceScreen` Class:** Handles the initial user interface with a button to start object detection.
- **`DetectionScreen` Class:** Manages the video feed, performs object detection, and updates the display with detection results.
- **`OsirisApp` Class:** The main Kivy application class that manages screen transitions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Kivy:** For providing the framework to build the graphical user interface.
- **OpenCV:** For video capture and image processing.
- **Ultralytics YOLO:** For the object detection model.
