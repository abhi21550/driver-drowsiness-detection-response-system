import cv2
import time
import serial
from geopy.geocoders import Nominatim
import geocoder
from twilio.rest import Client

# Arduino Serial Connection
arduino_port = 'COM7'  # Change if needed
baud_rate = 9600
try:
    arduino = serial.Serial(port=arduino_port, baudrate=baud_rate, timeout=1)
    print(f"Connected to Arduino on port {arduino_port} at {baud_rate} baud")
    time.sleep(2)  # Wait for Arduino to initialize
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Function to get current location
def get_current_location():
    geolocator = Nominatim(user_agent="eye_tracking_app")
    g = geocoder.ip('me')
    curr_loc = "8.4700516, 76.9802530"
    print(curr_loc)
    location = geolocator.geocode(curr_loc, language="en")
    return location.address if location else "Location not available"

# Twilio Setup
account_sid = 'id'
auth_token = 'token'
client = Client(account_sid, auth_token)
emergency_contact = 'phone number'

def send_twilio_message(message, location):
    client.messages.create(
        body=f"{message}\nLocation: {location}",
        from_='twilio number',
        to=emergency_contact
    )

# OpenCV Eye Detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
last_eye_detected_time = time.time()
FIRST_ALERT_TIME = 5  # Sleep alert at 5 sec
SECOND_ALERT_TIME = 10  # Danger alert at 10 sec

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(eyes) > 0:
        last_eye_detected_time = time.time()
        arduino.write(b'0')  # Send '0' if eyes are open
        time.sleep(0.1)  # Prevent serial overflow
        cv2.putText(frame, 'Eyes Open', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    else:
        cv2.putText(frame, 'Eyes Closed', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Sleep Alert
    if time.time() - last_eye_detected_time > FIRST_ALERT_TIME:
        print("Sleep Alert")
        arduino.write(b'1')  # Send '1' if no eyes detected
        time.sleep(0.1)

    # Danger Alert
    if time.time() - last_eye_detected_time > SECOND_ALERT_TIME:
        print("Danger! Sending Alert")
        current_location = get_current_location()
        send_twilio_message("Emergency: Eyes not detected for more than 10 seconds", current_location)
        break  # Stop program after emergency alert

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Reset the buzzer before exiting
print("Resetting buzzer...")
arduino.write(b'0')  # Turn off the buzzer
time.sleep(1)  # Allow the signal to be processed

cap.release()
cv2.destroyAllWindows()
arduino.close()
print("Program exited successfully!")

