import os
import cv2
import time
import glob
from emailcam import send_emaiL
from threading import Thread
import threading

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

status_list = []
count = 1
images_to_remove = []


# Checks if the imgs folder is created, if not it creates one.
def create_imgs_folder():
    if not os.path.exists("imgs"):
        os.makedirs("imgs")


def clean_folder():
    for image in images_to_remove:
        try:
            if os.path.exists(image):
                os.remove(image)
                print(f"Removed: {image}")
            else:
                print(f"File not found: {image}")
        except Exception as e:
            print(f"Error removing {image}: {e}")


create_imgs_folder()

while True:
    status = 0
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    faces = face_cascade.detectMultiScale(gray_frame_gau, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            image_path = f"imgs/{count}.png"
            cv2.imwrite(image_path, frame)
            count += 1
            status = 1
            images_to_remove.append(image_path)

    status_list.append(status)
    status_list = status_list[-2:]

    if len(status_list) >= 2 and status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_emaiL, args=(images_to_remove[-1],))
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

clean_folder()
video.release()
