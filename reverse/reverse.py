import cv2
from PIL import Image
import os

path_dir = './d/'
file_list = os.listdir(path_dir)

for input in file_list:
    imgread = './d/' + input
    print(imgread)
    src = cv2.imread('./d/' + input, cv2.IMREAD_COLOR)
    dst = cv2.bitwise_not(src)
    output = Image.fromarray(dst)
    output.save("./dr/" + input)
