from imutils import face_utils
import numpy as np
import math
import imutils
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

up_order = np.array([49, 50, 51, 52, 53, 54, 55, 65, 64, 63, 62, 61]) - 1
down_order = np.array([49, 61, 68, 67, 66, 65, 55, 56, 57, 58, 59, 60]) - 1

def color_lips(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		
		#Color lips
		cv2.fillPoly(image, [np.take(shape, up_order, 0)], (0,0, 255))
		cv2.fillPoly(image, [np.take(shape, down_order, 0)], (0, 0, 255))

	return image


def intersect(p1, p2, p3, p4):
	slope1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
	yinter1 = p1[1] - slope1 * p1[0]
	slope2 = (p4[1] - p3[1]) / (p4[0] - p3[0])
	yinter2 = p3[1] - slope2 * p3[0]
			
	res_x = (yinter2 - yinter1)/ (slope1 - slope2)
	res_y = slope1 * res_x + yinter1
			
	return (int(res_x), int(res_y))

def dist(p1, p2):
	return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def trans(p, r, phi):
	return (int(math.cos(phi) * r + p[0]), int(math.sin(phi) * r + p[1]))

def draw_glasses(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 1)

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		center = intersect(shape[37], shape[40], shape[38], shape[41])
		theta =  math.atan2(shape[39][1] - shape[36][1], shape[39][0] - shape[36][0]) 
		major_axis = int(dist(shape[39], shape[27]) * .7 + dist(center, shape[39]))
		minor_axis = int(dist(center, shape[19]) / 2 * 1.5) 
		thick1 = int(dist(shape[36], shape[39]) / 8)
		if (thick1 <= 0): thick1 = 1
		cv2.ellipse(image, center, (major_axis, minor_axis), theta / math.pi * 180, 0, 360, (122, 25, 25), thick1)
		cv2.ellipse(image, center, (major_axis - thick1 + 1, minor_axis - thick1 + 1), theta / math.pi * 180, 0, 360, (0, 0, 0), -1)
		g1 = trans(center, -major_axis, theta)
		g2 = trans(center, major_axis, theta)

		center = intersect(shape[43], shape[46], shape[44], shape[47])
		theta =  math.atan2(shape[45][1] - shape[42][1], shape[45][0] - shape[42][0])
		major_axis = int(dist(shape[42], shape[27]) * .7 + dist(center, shape[42]))
		minor_axis = int(dist(center, shape[24]) / 2 * 1.5) 
		thick2 = int(dist(shape[42], shape[45]) / 8)
		if (thick2 <= 0): thick2 = 1
		cv2.ellipse(image, center, (major_axis, minor_axis), theta / math.pi * 180, 0, 360, (122, 25, 25), thick2)
		cv2.ellipse(image, center, (major_axis - thick2 + 1, minor_axis - thick2 + 1), theta / math.pi * 180, 0, 360, (0, 0, 0), -1)
		g3 = trans(center, -major_axis, theta)
		g4 = trans(center, major_axis, theta)

		cv2.line(image, g2, g3, (122, 25, 25), (thick1 + thick2) // 2)
		cv2.line(image, g1, tuple(shape[0]), (122, 25, 25), thick1)
		cv2.line(image, g4, tuple(shape[16]), (122, 25, 25), thick2)
	
	return image
