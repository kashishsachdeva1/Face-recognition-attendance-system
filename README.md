# Face Recognition Attendance System

## Overview
This project is a **Face Recognition Attendance System** that uses OpenCV and the `face_recognition` library to detect and recognize faces from a webcam feed and mark attendance in a CSV file.

## Tech Stack
- **Python**
- **OpenCV** (Computer Vision Library)
- **face_recognition** (Dlib-based face recognition library)
- **NumPy** (Numerical Computation)
- **CSV** (Attendance Logging)
- **OS** (File Handling)
- **DateTime** (Timestamping Attendance)

## Features
- Real-time face recognition using a webcam
- Automatically detects and matches faces from a stored database
- Records attendance with timestamp in a CSV file
- Displays recognized face names in a live video feed

## Installation
### Prerequisites
Make sure you have **Python 3.x** installed.

### Install Required Libraries
Run the following command to install dependencies:
```bash
pip install opencv-python numpy face_recognition
```

## Folder Structure
```
Face_Recognition_Attendance/
│── imageBasic/       # Folder containing reference images
│── attendance.csv    # CSV file to store attendance records
│── face_recognition.py   # Main script for face recognition
```

## Usage
1. Place images of the people you want to recognize inside the `imageBasic/` folder.
2. Run the script:
   ```bash
   python face_recognition.py
   ```
3. The webcam will open, detect faces, and match them against stored images.
4. Recognized names will be displayed and stored in `attendance.csv`.
5. Press **'q'** to quit the webcam feed.

## How It Works
- Loads images from the `imageBasic/` directory and extracts face encodings.
- Captures live video frames, detects faces, and encodes them.
- Compares live face encodings with stored encodings.
- If a match is found, marks attendance in `attendance.csv` with the current timestamp.

## Example Output (CSV Format)
```
Name,Time
John,14:35:21
Alice,14:40:10
```

## Future Improvements
- Implement GUI for better user interaction
- Store attendance in a database instead of CSV
- Enable multi-camera support for larger environments



