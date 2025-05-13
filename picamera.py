from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()

# Configure the camera for still image capture
picam2.start()

# Give the camera a moment to adjust its settings
time.sleep(2)

# Capture an image and save it
picam2.capture_file("calibration_image.jpg")

# Stop the camera
picam2.stop()

print("Image captured successfully!")
