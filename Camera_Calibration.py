import numpy as np
import cv2

square_size = 38.1                                              #Checkerboard square size(in mm)
obj_points = []                                                 #3D points
img_points = []                                                 #2D points
pattern_size = (6, 4)                                           #Checkerboard pattern
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)                         #Generate an array for 3D coordinates
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size #An Array for 2D coordinates

image_paths = [                                                                             #Upload Images
    'Q3_pic1.jpg',                            #The Images are named Q3_pic1, Q3_pic2 and Q3_pic3
    'Q3_pic2.jpg',
    'Q3_pic3.jpg'
]

for image_path in image_paths:
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)                  #Find checkerboard corners

    if ret:
        obj_points.append(objp)
        img_points.append(corners)


if len(obj_points) > 0:
    ret, K, dist_coeff, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
    print("Camera Matrix, K is:")
    print(K)                                        

    if len(dist_coeff[0]) >= 2:                                                         #Check for distortion coefficients, 
        k1, k2, k3, k4, k5 = dist_coeff[0][:5]                                          #if more than 2 elements in list print k1 and k2
        print("Distortion Coefficients:")
        print(f"k1: {k1}")
        print(f"k2: {k2}")
        #print(f"k3: {k3}")
        #print(f"k4: {k4}")
        #print(f"k5: {k5}")
       
    elif len(dist_coeff[0]) == 1:                                                       #Fail-safe check
        k1 = dist_coeff[0]
        print("Distortion Coefficients are as follows:")
        print(f"k1: {k1}")
    else:
        print("Couldn't Find Distortion Coefficients")                                  #No distortion coefficients were found
else:
    print("Couldn't Detect Checkerboard")                           #Couldn't Load/Detect Image