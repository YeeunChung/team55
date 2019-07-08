import tensorflow as tf
import os
from PIL import Image
import numpy as np

height = 480
width = 640
predictwriter= tf.python_io.TFRecordWriter("predict.tfrecords")
predictdir = './input/'
eptlist=[]  #
for img_name in os.listdir(predictdir):
    eptlist.append(img_name)
lens=len(eptlist)
print(lens)
indexar=np.arange(lens)

randindex=np.random.permutation(indexar)
for indexx in randindex:
    filename = eptlist[indexx]
    imgraw = Image.open(predictdir+filename).convert('RGB')
    imgraw = imgraw.resize((width, height),Image.BILINEAR)
    imgraw = imgraw.tobytes()
    example = tf.train.Example(features=tf.train.Features(feature={
        'img': tf.train.Feature(bytes_list=tf.train.BytesList(value=[imgraw]))
    }))
    predictwriter.write(example.SerializeToString())
predictwriter.close()

