import numpy as np
from PIL import Image
import os

path_dir = './d/'
file_list = os.listdir(path_dir)

for input in file_list:
    image = Image.open(path_dir + input)
    pix = image.load()
    
    for i in range(640):
        for j in range(480):
            if pix[i, j] == 0:
                pix[i, j] = 255

    image.save('./new_d/' + input)
