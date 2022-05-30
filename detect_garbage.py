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

	imGray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(imGray, 127, 255, 0)

	contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours:
		x,y,w,h = cv2.boundingRect(contour)
		cv2.rectangle(blurred, (x,y), (x+w, y+h), (0,0,255), 2)
		

	cv2.imshow('frame', frame)
	cv2.imshow('Output', blurred)

	if cv2.waitKey(1) & 0xFF == ord('Q'):
	    break

cap.release()
output.release()

cv2.destroyAllWindows()
