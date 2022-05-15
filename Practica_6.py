import cv2
import numpy as np

def camera (hu_1, hu_2, s_1, s_2, v_1, v_2, hd_1, hd_2):
    r_d1 = np.array([hu_1, s_1, v_1], np.uint8)
    r_u1 = np.array([hu_2, s_2, v_2], np.uint8)

    r_d2 = np.array([hd_1, s_1, v_1], np.uint8)
    r_u2 = np.array([hd_2, s_2, v_2], np.uint8)
    
    while True:
        ret, frame = cap.read()
        if ret == True:
            HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            mask_r1 = cv2.inRange(HSV, r_d1, r_u1)
            mask_r2 = cv2.inRange(HSV, r_d2, r_u2)
            
            maskred = cv2.add(mask_r1, mask_r2)
            
            mask_r_v = cv2.bitwise_and(frame, frame, mask = maskred)        
            cv2.imshow('frame',frame)
            cv2.imshow('mask',maskred)
            cv2.imshow('mask v',mask_r_v)
            if cv2.waitKey(1) & 0xFF == ord('k'):
                break
    cap.release()
    cv2.destroyAllWindows()
    
cap = cv2.VideoCapture(0)
op = int(input("Rojo(1) - Verde (2) - Azul (3) - Amarillo (4):"))

if op == 1:
    camera(0, 8, 100, 255, 20, 255, 175, 179)

elif op == 2:
    camera(70, 80, 100, 255, 20, 255, 90, 100)
    
elif op == 3:
    camera(100, 120, 100, 255, 20, 255, 125, 130)
    
elif op == 4:
    camera(25, 30, 100, 255, 20, 255, 32, 36)
