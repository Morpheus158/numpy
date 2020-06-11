import numpy as np
from cv2 import cv2

myarr = np.random.randint(255, size=(1080,1920))

cv2.imwrite(r"numpy/img.png", myarr)