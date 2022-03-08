import cv2
import requests
import numpy as np
import imutils

#RGB values from RGB-tracking.py
min_blue, min_green, min_red = 0, 0, 125
max_blue, max_green, max_red = 146, 87, 255

v = cv2.__version__.split('.')[0]

url = "http://192.168.0.106:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)

    frame_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_HSV,
                       (min_blue, min_green, min_red),
                       (max_blue, max_green, max_red))
    cv2.namedWindow('Binary frame with Mask', cv2.WINDOW_NORMAL)
    cv2.imshow('Binary frame with Mask', mask)

    if v == '3':
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                          cv2.CHAIN_APPROX_NONE)

    else:
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    contours = sorted(contours, key = cv2.contourArea, reverse=True)

    if contours:
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(contours[0])
        cv2.rectangle(img, (x_min - 15, y_min - 15),
                      (x_min + box_width + 15, y_min + box_height + 15),
                      (225, 0, 0), 3)
        label = 'BLue Color'
        cv2.putText(img, label, (x_min - 5, y_min -25),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (225, 0, 0), 2)

    cv2.namedWindow('Streaming Cam', cv2.WINDOW_NORMAL)
    cv2.imshow('Streaming Cam', img)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

cv2.destroyAllWindows()

