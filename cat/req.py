import cv2
import numpy as np
import serial
import time

cap = cv2.VideoCapture(0)
portNo = "/dev/cu.usbserial-1430"
vart = serial.Serial(portNo, 9600)

while(True):
    t = time.localtime() 
    current_time = time.strftime("%H", t)     
    if current_time == "08" or current_time == "14" or current_time =="17":
        msg = "2"
        msg = bytes(str(msg), "utf-8")
        vart.write(msg)
        print(msg)
        time.sleep(1)
    
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    frameresized = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    hsv = cv2.blur(hsv, (5, 5))  
    mask = cv2.inRange(hsv, (143, 95, 75), (179, 255, 255))

    lower_blue = np.array([38, 86, 0])    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    counturs = sorted(contours, key=cv2.contourArea, reverse=True)   
    if len(counturs) > 3:
        msg = "1"
        msg = bytes(str(msg), "utf-8")
        vart.write(msg)
        print(msg)
        flag = True

    for contour in counturs:
    
        cv2.drawContours(frame, counturs[0], -1, (255, 0, 255), 3)
        cv2.imshow("Counturs", frame)
  
    key = cv2.waitKey(1) 
    time.sleep(1)


cap.release()
cv2.destroyAllWindows()