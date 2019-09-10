from model import color_lips, draw_glasses
import cv2

webcam = cv2.VideoCapture(0)
while (True):
	image = webcam.read()[1]
	color_lips(image)
	draw_glasses(image)	
	cv2.imshow("Colored lips", image)
	if (cv2.waitKey(1) & 0xFF == ord('q')): break

webcam.release()
cv2.destroyAllWindows()
