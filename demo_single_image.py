from model import color_lips, draw_glasses
import cv2

#Change this to your desired image directory
image = cv2.imread('./sample_images/trump.jpg')
color_lips(image)
draw_glasses(image)	
cv2.imshow("Colored lips", image)
cv2.waitKey(0); cv2.destroyAllWindows()
