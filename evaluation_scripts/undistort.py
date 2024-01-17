import os
import cv2
import numpy as np

fx = 932.94
fy = 959.83
ppx = 950.90
ppy = 429.73
xi = 0.252
image_dir = '/home/ubuntu/droidimgs'
output_dir = '/home/ubuntu/undistorted'

camera_matrix = np.array([
    [fx, 0.0, ppx],
    [0.0, fy, ppy],
    [0.0, 0.0, 1.0],
])

dist_coeffs = np.array([xi, 0.0, 0.0, 0.0, 0.0])

imgs = os.listdir(image_dir)
for path in imgs:
    img = cv2.imread(os.path.join(image_dir, path))
    undistorted_img = cv2.undistort(img, camera_matrix, dist_coeffs)
    cv2.imwrite(os.path.join(output_dir, os.path.basename(path)), undistorted_img)
