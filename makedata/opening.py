# https://webnautes.tistory.com/1257
import cv2
import numpy as np
import os
from PIL import Image

path_dir = './new_d/'
file_list = os.listdir(path_dir)

for input in file_list:
    img = cv2.imread(path_dir + input, 0)
    
    kernel = np.ones((3, 3), np.uint8)
    result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    output = Image.fromarray(result)
    output.save('./d_closed2/' + input)
