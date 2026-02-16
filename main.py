import cv2
import numpy as np


def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
    
        detected_frame = detect(frame)
        

def detect(frame):
    img = frame  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    th_otsu, Th_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(Th_otsu, cv2.MORPH_OPEN, kernel, iterations=2)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    num_labels, labeled_img, stats, centroid = cv2.connectedComponentsWithStats(closing, connectivity=8)
    annonated = cv2.cvtColor(labeled_img, cv2.COLOR_GRAY2BGR)

    

