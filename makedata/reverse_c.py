import cv2
from PIL import Image
import os

path_dir = './c/'
file_list = os.listdir(path_dir)
f = open('./emptylist_c_1.txt', 'w')

for input in file_list:
    src = cv2.imread('./c/' + input, cv2.IMREAD_GRAYSCALE)
    if src is None:
        print(input)
        f.write(input + ' ')

f.close()
