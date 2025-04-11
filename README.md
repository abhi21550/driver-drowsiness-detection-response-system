*A real-time AI-powered eye tracking safety solution for fatigue detection and emergency response.*

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Arduino](https://img.shields.io/badge/Arduino-Connected-green?style=flat-square&logo=arduino)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange?style=flat-square&logo=opencv)
![Twilio](https://img.shields.io/badge/Twilio-Alert%20System-red?style=flat-square&logo=twilio)

---

## 🚨 What is DDDRS?

**Driver Drowsiness Detection and Response System (DDDRS)** is an innovative eye-tracking safety system that detects fatigue or unconsciousness using a webcam, OpenCV, and Arduino. When the system detects closed eyes for extended durations, it:

- 🚨 Triggers a buzzer via Arduino  
- 📍 Tracks and fetches real-time location  
- 📲 Sends an emergency SMS with location using Twilio  

---

## ⚙️ How It Works

1. 👁️ Detects eyes using Haar cascades in OpenCV  
2. ⏱️ Monitors if eyes stay closed beyond thresholds  
3. 📡 Fetches real-time location using geocoder & geopy  
4. 🔊 Activates buzzer via Arduino  
5. 📲 Sends SMS alert with location using Twilio  

---

## 🧠 Tech Stack

| Component       | Purpose                         |
|----------------|----------------------------------|
| `Python`       | Main application logic           |
| `OpenCV`       | Real-time eye tracking           |
| `Arduino`      | Buzzer alarm control             |
| `Twilio API`   | Emergency SMS alerts             |
| `Geopy & Geocoder` | Real-time location detection |

---

## 🧪 Setup Instructions

### 🔧 Hardware Requirements

- Arduino Uno/Nano
- Buzzer
- USB Cable
- Webcam

### 💻 Software Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DDDRS.git
   cd DDDRS
2. **Install dependencies**
   ```bash
    pip install opencv-python geopy geocoder twilio

3.**Upload ddrsuno.ino to your Arduino using the Arduino IDE.**

4. **Configure Credentials in the Python script:**
   ```bash
     Twilio SID, Auth Token, From Number, and To Number

5. **Run the system**
      ```bash
      python dddrs_finalworking.py

📍 Example Emergency Message
🚨 Emergency: Eyes not detected for more than 10 seconds
📍 Location: Sree Chitra Thirunal College of Engineering, Trivandrum, Kerala, India

📁 **Project Structure**

📦DDDRS
 ┣ 📜dddrs_eye_tracker.py        ← Main Python script
 ┣ 📜ddrsuno.ino                 ← Arduino sketch
 ┗ 📄README.md                   ← Project documentation
