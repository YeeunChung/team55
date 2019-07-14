import os
from PIL import Image

c_path_dir = './val_c/'
d_path_dir = './val_d/'
c_file_list = os.listdir(c_path_dir)
d_file_list = os.listdir(d_path_dir)

fc = open('./c.txt', 'w')
fd = open('./d.txt', 'w')

for file in c_file_list:
    num = file[1:-4]
    dfile = 'd' + num + '.png'
    if dfile not in d_file_list:
        fc.write(file + '\n')

for file in d_file_list:
    num = file[1:-4]
    cfile = 'c' + num + '.jpg'
    if cfile not in c_file_list:
        fd.write(file + '\n')

fc.close()
fd.close()
