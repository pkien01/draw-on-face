# draw-on-face

This is mostly 

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