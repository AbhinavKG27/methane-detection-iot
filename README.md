# Detection of Methane Gas and Monitoring Cow Health in Dairy Farms

An IoT + Machine Learning based smart dairy farm monitoring system for real-time methane detection, environmental monitoring, and early health risk prediction.

## Features

- Real-time methane monitoring using MQ-4 sensor
- Temperature and humidity monitoring using DHT22
- ESP32-based IoT communication
- Cloud integration using Firebase/MQTT
- Machine Learning-based methane prediction
- Dashboard visualization
- SMS/Email alerts

## Hardware Used

- ESP32
- MQ-4 Methane Sensor
- MQ-135 Air Quality Sensor
- DHT22 Sensor
- Relay Module
- Buzzer
- LEDs

## Software Stack

- Arduino IDE
- Python
- Flask/Django
- Firebase
- TensorFlow / Scikit-learn

## System Architecture

Sensors → ESP32 → Cloud → ML Model → Dashboard → Alerts

## Installation

### ESP32 Firmware

1. Open Arduino IDE
2. Install ESP32 board package
3. Install required libraries:
   - DHT sensor library
   - WiFi library
   - Firebase ESP Client
4. Upload firmware

### Python Dashboard

```bash
pip install -r requirements.txt
python app.py

Future Enhancements
TinyML support
Automatic ventilation control
Mobile application
Multi-farm monitoring