# Face Detection with OpenCV (Haar Cascade)

This project implements face detection using OpenCV and the Haar Cascade model. There are two versions available: one for detecting faces from a static image and another for detecting faces from a video stream (using the laptop's camera).

## Technologies Used
- **Python 3.x**
- **OpenCV**: for image processing and face detection using the Haar Cascade model.
- **imutils**: for image resizing and handling.
- **argparse**: for managing command-line arguments.

## Installation

Make sure to install the required packages using `pip`:

pip install opencv-python imutils


1. Face Detection from an Image
Description

This script allows you to detect faces in a static image by loading the image from a file and drawing rectangles around the detected faces.
How to Use:

    Save the desired image you want to analyze.

    Run the script with the following arguments:

What the script does:

    Loads the specified image.
    Applies the Haar Cascade model to detect faces.
    Draws rectangles around the detected faces.
    Displays the image with highlighted faces.


2. Face Detection from Video Stream (Laptop Camera)
Description

This script allows face detection in real-time from the video stream of the laptop's camera. Detected faces are highlighted during video playback.

What the script does:

    Opens the laptop's camera and starts capturing video frames.
    Applies the Haar Cascade model to detect faces in each frame.
    Draws rectangles around the detected faces in real-time.
    Displays the video stream with highlighted faces.

No problem! Here's the README.md file in English:

# Face Detection with OpenCV (Haar Cascade)

This project implements face detection using OpenCV and the Haar Cascade model. There are two versions available: one for detecting faces from a static image and another for detecting faces from a video stream (using the laptop's camera).

## Technologies Used
- **Python 3.x**
- **OpenCV**: for image processing and face detection using the Haar Cascade model.
- **imutils**: for image resizing and handling.
- **argparse**: for managing command-line arguments.

## Installation

Make sure to install the required packages using `pip`:

```bash
pip install opencv-python imutils

1. Face Detection from an Image
Description

This script allows you to detect faces in a static image by loading the image from a file and drawing rectangles around the detected faces.
How to Use:

    Save the desired image you want to analyze.

    Run the script with the following arguments:

    python face_detect_image.py --image <path_to_image>

        --image: path to the image file you want to analyze.

Example Run:

python face_detect_image.py --image image.jpg

What the script does:

    Loads the specified image.
    Applies the Haar Cascade model to detect faces.
    Draws rectangles around the detected faces.
    Displays the image with highlighted faces.

Code:

import cv2
import argparse

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the input image and convert to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

2. Face Detection from Video Stream (Laptop Camera)
Description

This script allows face detection in real-time from the video stream of the laptop's camera. Detected faces are highlighted during video playback.
How to Use:

    Open your laptop's camera.
    Run the script:

    python face_detect_video.py

What the script does:

    Opens the laptop's camera and starts capturing video frames.
    Applies the Haar Cascade model to detect faces in each frame.
    Draws rectangles around the detected faces in real-time.
    Displays the video stream with highlighted faces.


Contributions

If you have suggestions or improvements for this project, feel free to open a pull request!


License

This project is licensed under the MIT License.

