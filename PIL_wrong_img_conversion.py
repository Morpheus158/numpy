from cv2 import cv2
from PIL import Image

wall = cv2.imread(r"numpy/lara.png",1)
pil_img = Image.fromarray(wall)
pil_img.save(r"numpy/myimg.png")