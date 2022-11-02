# program to capture single image from webcam in python

# importing OpenCV library
from cv2 import *
from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyWindow
# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 0
cam =VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:

	# showing result, it take frame name and image
	# output
	imshow("captured_img", image)

	# saving image in local storage
	imwrite("captured_img.png", image)

	# If keyboard interrupt occurs, destroy image
	# window
	waitKey(0)
	destroyWindow("captured_img")


# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")

