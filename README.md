# THE THIRD EYE – SMART CANE USING RASPBERRY PI

## Overview
THE THIRD EYE is an innovative assistive device designed to aid visually impaired individuals with independent navigation. Using a Raspberry Pi at its core, this project integrates advanced technologies like object detection through ResNet, GPS for navigation, and voice feedback to enhance mobility and safety for blind users.

## Features
- **Object Detection:** Utilizes a Raspberry Pi integrated with a Logitech C270 camera to detect obstacles.
- **Voice-Based Assistance:** Provides audio feedback through earphones connected to the Raspberry Pi, offering real-time navigation and obstacle information.
- **GPS Navigation:** Includes a GPS module that aids in outdoor navigation by providing accurate location data.
- **Real-Time Feedback:** Incorporates an ultrasonic sensor to detect close-range obstacles, enhancing the cane's utility and safety.

## Technologies Used
- **Raspberry Pi 4**: Main computing unit.
- **Python**: Primary programming language.
- **ResNet**: Used for object detection.
- **TensorFlow**: Supports the machine learning models.
- **GPS and GSM Modules**: For location tracking and data communication.

## Hardware Components
- Raspberry Pi 4
- Logitech C270 HD Webcam
- HC-SRO4 Ultrasonic Sensor
- GPS Module
- GSM Module

## Installation
### Prerequisites
- Raspberry Pi OS installed on your Raspberry Pi.
- Python 3.x
- TensorFlow and other Python libraries such as NumPy and OpenCV.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/nandutejaswini/the-third-eye.git
