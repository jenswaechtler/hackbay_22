import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower = np.array([19, 111, 90])
upper = np.array([57, 227, 255])

while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower, upper)
	color_filtered = cv2.bitwise_and(frame,frame, mask= mask)
	
	blurred = cv2.medianBlur(color_filtered, 9)


	cv2.imshow('frame', frame)
	cv2.imshow('Output', blurred)

	if cv2.waitKey(1) & 0xFF == ord('Q'):
	    break

cap.release()
output.release()

cv2.destroyAllWindows()
