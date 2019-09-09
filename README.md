# draw-on-face

This is a program that automatically draws glasses and colors the lips of human faces based on 68 facial landmarks detected using a trained model from [this website](https://www.pyimagesearch.com/2017/04/10/detect-eyes-nose-lips-jaw-dlib-opencv-python/).



## Installation and running demo

Prerequisites: Make sure that you've installed all of the necessary packages and libraries, including imutils, numpy, dlib, and opencv (cv2).

1.  Clone this repository

   ```bash
   git clone https://github.com/pkien01/draw-on-face
   ```

2. Download the pretrained weights for facial landmarks detection [here](https://drive.google.com/file/d/12583GxL9ospcvv7oaRkRD0oY-eLhuw9_/view?usp=sharing) and put it inside the `draw-on-face` folder. The facial landmark detector implemented inside dlib produces 68 *(x, y)*-coordinates that map to *specific facial structures*. These 68 point mappings were obtained by training a shape predictor on the labeled [iBUG 300-W dataset](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/). 

3. Open the terminal in the `draw-on-face` folder, or type the following in terminal

   ```bash
   cd draw-on-face
   ```

4. To run demo on a sample image

   ```bash
   python3 demo_single_image.py
   ```

   You can also open the file `demo_single_image.py` in a text editor and change the following line to your custom image location. Then rerun the demo.

   ```python
   #Change this to your desired image directory
   image = cv2.imread('./sample_images/trump.jpg')
   ```

5. To run demo on webcam

   ```bash
   python3 demo_webcam.py
   ```

You can modify the code of the file `demo_single_image.py` or `demo_webcam.py` so that it only draw glasses, color lips, or both by adjusting the following lines

```python
color_lips(image)
draw_glasses(image)
```



## Draw your own objects based on the 68 facial landmarks

In the file `model.py`, you can create a new function as follows

```python
def draw_own_object(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		
		#Draw your own objects based on the landmarks stored in the 'shape' array

	return image
```



<img src="https://www.pyimagesearch.com/wp-content/uploads/2017/04/facial_landmarks_68markup-768x619.jpg" alt="Visualizing each of the 68 facial coordinate points" style="zoom: 67%;" />



<div align="center">Visualizing each of the 68 facial coordinate points</div>


You can use [drawing functions](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html) in OpenCV in order to draw different shapes to form cool objects on the face. Note that the indexes in the diagram above need to be subtracted by 1 to access the position of the landmark. For example, in order to access the coordinates of the tip of the nose (point 34 in the above diagram), you need to use `shape[33]`. Similarly, if you want to find the coordinates of the leftmost rear of the face (point 1), you need to use `shape[0]`. 



## Results

Here are the results from some sample images



<img src="https://raw.githubusercontent.com/pkien01/draw-on-face/master/sample_images/obama_colored.jpg" style="zoom: 30%" />



<img src="https://raw.githubusercontent.com/pkien01/draw-on-face/master/sample_images/trump_colored.jpg" style="zoom: 70%" />



<img src="https://raw.githubusercontent.com/pkien01/draw-on-face/master/sample_images/hiccup_colored.jpg" style="zoom: 50%" />



Enjoy!

## Contacts

If you have any questions or found some serious errors/bugs in the code, you can kindly write an email to phamkienxmas2001@gmail.com, v.kienp16@vinai.io, or leave a message below on GitHub. Thank you!
