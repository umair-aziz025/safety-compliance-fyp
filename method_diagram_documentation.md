# Safety Compliance Detection System - Method Diagram

## Professional Method/Workflow Diagram

This document contains the method diagram for our Safety Compliance Detection System focused on three critical PPE classes: **Helmet, Vest, and Mask**.

### System Architecture Overview

The system follows a comprehensive workflow from user input to detection results, incorporating:
- **Authentication & User Management**
- **Video Processing Pipeline** (Webcam + Upload)
- **YOLOv8 Detection Engine**
- **Real-time Tracking & Compliance Analysis**
- **Database Storage & Reporting**

### Method Diagram

![Method Diagram](method_diagram.svg)

### Key Features Highlighted in Diagram:

1. **Input Sources**: Webcam feed and video file upload
2. **Detection Engine**: YOLOv8l model optimized for helmet, vest, and mask
3. **Real-time Processing**: EuclideanDistTracker for object tracking
4. **Compliance Analysis**: Safety status evaluation and alerts
5. **Visual Feedback**: Color-coded overlays and PNG icons
6. **Database Integration**: Session tracking and audit trails

### Technology Stack:
- **Frontend**: HTML5, Bootstrap, jQuery
- **Backend**: Flask (Python)
- **AI Model**: YOLOv8l (Ultralytics)
- **Database**: PostgreSQL
- **Computer Vision**: OpenCV
- **Authentication**: bcrypt, session management

### Performance Metrics:
- **Overall mAP@0.5**: 0.966
- **Real-time Processing**: 21.5 FPS (GPU enabled)
- **Helmet Detection**: 98.4% mAP@0.5
- **Vest Detection**: 94.1% mAP@0.5  
- **Mask Detection**: 97.4% mAP@0.5
