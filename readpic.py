import numpy as np
from PIL import Image
import os

path_dir = './stop/'
file_list = os.listdir(path_dir)

from input in file_list:
    image = Image.open(path_dir + input)

    

