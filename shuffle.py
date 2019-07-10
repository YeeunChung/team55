#-*- coding: utf-8 -*-
import os
import random
from PIL import Image

c_path_dir = './c/'
d_path_dir = './d/'
c_file_list = os.listdir(c_path_dir)
d_file_list = os.listdir(d_path_dir)
file_length = len(c_file_list) #c, d 개수똑같음

train_length = file_length * 8 / 10
val_length = file_length - train_length

c_train_list = random.sample(c_file_list, train_length)
c_val_list = []

for file in c_file_list:
    if file not in c_train_list:
        c_val_list.append(file)

# store d_train_list, d_val_list
d_train_list = []
d_val_list = []
for file in c_train_list:
    num = file[1:-4] # 숫자만 추출
    dfile = 'd' + num + '.png'
    d_train_list.append(dfile)
for file in c_val_list:
    num = file[1:-4]
    dfile = 'd' + num + '.png'
    d_val_list.append(dfile)

# 저장
for file in c_train_list:
    img = Image.open(c_path_dir + file)
    img.save('./train_c/' + file)
for file in c_val_list:
    img = Image.open(c_path_dir + file)
    img.save('./val_c/' + file)
for file in d_train_list:
    img = Image.open(d_path_dir + file)
    img.save('./train_d/' + file)
for file in d_val_list:
    img = Image.open(d_path_dir + file)
    img.save('./val_d/' + file)
