# PPE Safety Compliance Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-orange.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

The **PPE Safety Compliance Detection System** is an advanced AI-powered web application designed to monitor and enforce Personal Protective Equipment (PPE) compliance in workplace environments. Using state-of-the-art computer vision technology (YOLOv8), the system provides real-time detection and comprehensive tracking of safety equipment usage, helping organizations maintain workplace safety standards and regulatory compliance.

### Key Features

- **🔍 Real-Time Detection**: Monitor PPE compliance through live webcam feeds
- **📹 Video Analysis**: Upload and analyze recorded videos for compliance auditing
- **👥 Multi-User Management**: Complete authentication system with role-based access control
- **📊 Admin Dashboard**: Comprehensive analytics and user management interface
- **📈 Session Tracking**: Detailed logging of all detection sessions and user activities
- **🎛️ Configurable Thresholds**: Adjustable confidence levels for different environments
- **⚡ GPU Acceleration**: CUDA support for faster processing
- **📝 Detailed Reporting**: Export compliance data and activity logs

## 🛡️ PPE Detection Capabilities

The system can detect and verify the following safety equipment:

- ✅ **Safety Helmets / Hard Hats**
- ✅ **High-Visibility Vests**
- ✅ **Face Masks**

Each detection provides:
- Object tracking with unique IDs
- Confidence scores
- Compliance status (safe/unsafe)
- Frame-by-frame analysis
- Exportable logs and reports

## 🏗️ System Architecture

### Technology Stack

#### Backend
- **Framework**: Flask 2.3.3
- **Database**: PostgreSQL with psycopg2
- **Authentication**: bcrypt password hashing
- **Session Management**: Flask sessions with caching

#### AI/ML
- **Object Detection**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV (cv2)
- **Deep Learning**: PyTorch with CUDA support
- **Tracking**: ASOne multi-object tracking

#### Frontend
- **UI Framework**: Bootstrap 3.3.7
- **Forms**: Flask-WTF with WTForms validation
- **Real-time Updates**: AJAX with jQuery
- **Responsive Design**: Mobile-friendly interface

#### Data & Analytics
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib, Seaborn
- **Configuration**: python-dotenv

## 📋 Prerequisites

### System Requirements

- **Operating System**: Windows 10/11, Linux, or macOS
- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended for GPU processing)
- **Storage**: At least 5GB free space
- **GPU** (Optional): NVIDIA GPU with CUDA support for faster processing

### Software Dependencies

- PostgreSQL 12+ (Database server)
- Git (Version control)
- Modern web browser (Chrome, Firefox, Edge)

## 🚀 Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/umair-aziz025/safety-compliance-fyp.git
cd safety-compliance-fyp
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Database Setup

1. Install PostgreSQL and create a database:

```sql
CREATE DATABASE ppe_safety_db;
CREATE USER ppe_admin WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE ppe_safety_db TO ppe_admin;
```

2. Configure the `config.env` file:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://ppe_admin:your_secure_password@localhost:5432/ppe_safety_db
```

### 5. Initialize the Application

```bash
python flaskApp_with_auth.py
```

The system will automatically:
- Create necessary database tables
- Set up indexes for performance
- Create a default admin account

### 6. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

**Default Admin Credentials:**
- Email: `admin@safetysystem.com`
- Password: `admin123`

⚠️ **Important**: Change the default admin password immediately after first login!

## 📖 User Guide

### For Administrators

1. **Dashboard Access**
   - Login with admin credentials
   - Access admin dashboard from the navigation menu
   - View system statistics and recent activities

2. **User Management**
   - Approve/reject new user registrations
   - Suspend or reactivate user accounts
   - Delete users if necessary
   - View user activity logs

3. **Session Monitoring**
   - Review all detection sessions
   - Filter by session type (webcam/video upload)
   - Export compliance reports
   - Analyze detection statistics

### For Regular Users

1. **Registration & Login**
   - Register a new account with company details
   - Wait for admin approval
   - Login after approval

2. **Video Upload Detection**
   - Navigate to the main application page
   - Upload a video file (MP4, AVI, MOV)
   - Adjust confidence threshold (0-100%)
   - Click "Run" to start detection
   - View real-time results and download processed video

3. **Webcam Detection**
   - Click "Start Webcam" button
   - Allow camera permissions
   - Monitor live PPE compliance
   - Stop detection and save results

4. **Profile Management**
   - Update personal information
   - Change password
   - View detection history

## 🔧 Configuration

### Environment Variables (`config.env`)

```env
# Flask Configuration
SECRET_KEY=your_flask_secret_key_here
DEBUG=False

# Database Configuration
DATABASE_URL=postgresql://username:password@host:port/database

# Upload Configuration (Optional)
MAX_CONTENT_LENGTH=100000000  # 100MB max file size

# CUDA Configuration (Optional)
CUDA_VISIBLE_DEVICES=0  # GPU device ID
```

### Model Configuration

The YOLOv8 model file (`best.pt`) should be placed in the project root directory. You can:
- Use the pre-trained model included
- Train your own model on custom PPE datasets
- Adjust confidence thresholds in the web interface

## 📊 Database Schema

### Users Table
- User authentication and profile information
- Role-based access control (admin/customer)
- Status management (pending/approved/rejected/suspended)

### User Activity Logs
- Comprehensive activity tracking
- IP address and user agent logging
- Detection result storage

### Detection Sessions
- Session type tracking (webcam/video)
- Performance metrics (duration, detection counts)
- Compliance statistics (safe/unsafe ratios)

## 🎯 Use Cases

### 1. Construction Sites
- Monitor hard hat and vest compliance
- Real-time alerts for safety violations
- Daily compliance reports for supervisors

### 2. Manufacturing Facilities
- Ensure PPE usage in restricted areas
- Track compliance trends over time
- Generate safety audit reports

### 3. Healthcare Facilities
- Monitor mask compliance
- Visitor and staff screening
- Infection control compliance tracking

### 4. Industrial Plants
- Multi-PPE requirement enforcement
- Zone-based compliance monitoring
- Incident prevention and documentation

## 📈 Performance Optimization

### GPU Acceleration

Enable CUDA for faster processing:

```python
# Toggle CUDA in the web interface
# Or set in session manually
session['use_cuda'] = True
```

### Processing Tips

- **Confidence Threshold**: Start with 25-30% for general use
- **Video Quality**: Higher resolution improves accuracy but slows processing
- **Frame Rate**: Lower frame rates reduce processing time
- **Batch Processing**: Process multiple videos during off-peak hours

## 🔒 Security Features

- **Password Hashing**: bcrypt with salt
- **SQL Injection Protection**: Parameterized queries
- **Session Security**: Secure session cookies
- **CSRF Protection**: Flask-WTF CSRF tokens
- **Input Validation**: WTForms validators
- **Role-Based Access**: Admin-only endpoints protected

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check DATABASE_URL in config.env
   - Ensure database user has proper permissions

2. **Webcam Not Working**
   - Check camera permissions in browser
   - Verify no other application is using the camera
   - Try restarting the browser

3. **Slow Processing**
   - Enable CUDA if GPU available
   - Reduce video resolution
   - Lower confidence threshold
   - Close other applications

4. **Import Errors**
   - Ensure all dependencies are installed
   - Activate virtual environment
   - Run `pip install -r requirements.txt` again

## 📁 Project Structure

```
safety-compliance-fyp/
│
├── flaskApp_with_auth.py       # Main application with authentication
├── hubconfCustom.py             # Custom YOLO detection module
├── tracker.py                   # Object tracking implementation
├── config.env                   # Environment configuration
├── requirements.txt             # Python dependencies
├── best.pt                      # YOLOv8 model weights
│
├── templates/                   # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── video.html
│   ├── admin_dashboard.html
│   └── ...
│
├── static/                      # Static files
│   ├── files/                   # Uploaded videos
│   └── css/                     # Stylesheets
│
├── data/                        # Detection results
│   └── tracking_results.txt
│
├── Dataset/                     # Training dataset
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
│
├── asone/                       # ASOne tracking library
│   ├── detectors/
│   └── trackers/
│
└── utils/                       # Utility scripts
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Authors

- **Umair Aziz** - *Initial work* - [umair-aziz025](https://github.com/umair-aziz025)

## 🙏 Acknowledgments

- **Ultralytics** for YOLOv8 implementation
- **Flask** community for excellent documentation
- **OpenCV** for computer vision tools
- **PostgreSQL** for robust database management

## 📧 Contact & Support

For questions, issues, or suggestions:

- **GitHub Issues**: [Create an issue](https://github.com/umair-aziz025/safety-compliance-fyp/issues)
- **Email**: umair.aziz025@example.com

## 🔮 Future Enhancements

- [ ] Mobile application for iOS/Android
- [ ] Multi-camera support for large facilities
- [ ] SMS/Email alerts for safety violations
- [ ] Advanced analytics with machine learning insights
- [ ] Integration with existing HR/Safety systems
- [ ] Multi-language support
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] API endpoints for third-party integration
- [ ] Custom PPE type training interface
- [ ] Zone-based detection rules

## 📊 System Requirements Summary

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | Dual-core 2.0 GHz | Quad-core 3.0 GHz+ |
| RAM | 8 GB | 16 GB+ |
| GPU | Integrated | NVIDIA GTX 1060+ |
| Storage | 5 GB | 20 GB SSD |
| Network | 10 Mbps | 50 Mbps+ |

---

**⭐ If you find this project helpful, please consider giving it a star!**

**Made with ❤️ for workplace safety**
