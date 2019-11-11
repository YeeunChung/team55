#-*-coding: utf-8 -*-
import argparse
import os
import numpy as np
import tensorflow as tf
import cv2
import time
from matplotlib import pyplot as plt
from PIL import Image
import time
import models

                
def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', help='Converted parameters for the model')
    args = parser.parse_args()

    cap = cv2.VideoCapture('nvcamerasrc sensor-id=0 fpsRange=\"1 30\" ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink')
    
    # Default input size
    height = 480
    width = 640
    channels = 3
    batch_size = 1

    # Create a placeholder for the input image
    input_node = tf.placeholder(tf.float32, shape=(None, height, width, channels))
    # Construct the network
    net = models.ResNet50UpProj({'data': input_node}, batch_size, 1, False)
        
    with tf.Session() as sess:

        # Load the converted parameters
        print('Loading the model')

        # Use to load from ckpt file
        saver = tf.train.Saver()
        saver.restore(sess, args.model_path)
        
        path_dir = './STOP/'
        file_list = os.listdir(path_dir)
        f = open('./predict_timetest.txt', 'w')
        
        count_go = 150
        count_stop = 0
        for input in file_list:
            start = time.time()
            frame = Image.open(path_dir + input)
            # Read image
            img = frame
            img = np.array(img).astype('float32')
            img = np.expand_dims(np.asarray(img), axis = 0)
        
            # Evalute the network for the given image
            evaluate = sess.run(net.get_output(), feed_dict={input_node: img})
            tf.get_variable_scope().reuse_variables()
            
            pred = evaluate[0,:,:,0]
            status = 'go'
            for i in range(80, 161):
                for j in range(100, 221):
                    if pred[i][j] < 1.0:
                        status = 'stop'
                        count_go = count_go - 1
                        count_stop = count_stop + 1
                        break
            print("time : ", time.time() - start)
            print(input + ': ' + status)
            f.write(input + ': ' + status + '\n')

    print('go ' + str(count_go) + '개')
    print('stop ' + str(count_stop) + '개')

    f.write('go ' + str(count_go) + '개\n')
    f.write('stop ' + str(count_stop) + '개\n')
    f.close() 
    os._exit(0)

if __name__ == '__main__':
    main()

        



