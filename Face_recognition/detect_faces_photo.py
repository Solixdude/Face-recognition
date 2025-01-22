import cv2
import argparse
import tkinter as tk

# Argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# Load Haar Cascade model
haar_cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Load the input image and convert to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Get screen dimensions to adjust image size
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Resize the image to fit within the screen dimensions
max_width = int(screen_width * 0.8)  # Use 80% of the screen width
if image.shape[1] > max_width:
    scale = max_width / image.shape[1]
    new_dim = (max_width, int(image.shape[0] * scale))
    image = cv2.resize(image, new_dim)

# Show the resized image
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
