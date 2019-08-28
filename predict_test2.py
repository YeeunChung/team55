#-*-coding: utf-8 -*-
from socket import *
import argparse
import os
import numpy as np
import tensorflow as tf
import cv2
import time
from matplotlib import pyplot as plt
from PIL import Image

import models

def predict(model_data_path, frame):

    
    # Default input size
    height = 480
    width = 640
    channels = 3
    batch_size = 1
   
    # Read image
    # img = Image.open(image_path)
    img = frame
    #img = img.resize([width,height], Image.ANTIALIAS)
    img = np.array(img).astype('float32')
    img = np.expand_dims(np.asarray(img), axis = 0)
   
    # Create a placeholder for the input image
    input_node = tf.placeholder(tf.float32, shape=(None, height, width, channels))

    # Construct the network
    net = models.ResNet50UpProj({'data': input_node}, batch_size, 1, False)
        
    with tf.Session() as sess:

        # Load the converted parameters
        print('Loading the model')

        # Use to load from ckpt file
        saver = tf.train.Saver()
        saver.restore(sess, model_data_path)

        # Use to load from npy file
        #net.load(model_data_path, sess) 

        # Evalute the network for the given image
        pred = sess.run(net.get_output(), feed_dict={input_node: img})
        tf.get_variable_scope().reuse_variables()
        
        # Plot result
        #fig = plt.figure()
        #ii = plt.imshow(pred[0,:,:,0], interpolation='nearest')
        #fig.colorbar(ii)
        #plt.show()
        #plt.pause(0.001)
        
        return pred[0,:,:,0]
        
                
def main():
    # Parse arguments
    c = socket(AF_INET, SOCK_DGRAM)
    host_ip = '15.164.99.163'
    host_port = 9999
    c.bind(('', 0))
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', help='Converted parameters for the model')
    #parser.add_argument('image_paths', help='Directory of images to predict')
    args = parser.parse_args()
    cap = cv2.VideoCapture('nvcamerasrc sensor-id=0 fpsRange=\"1 30\" ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink')
    
    while True:
        #print(1)
        ret, frame = cap.read()
        pred = predict(args.model_path, frame)
        
        status = 'go'
        for i in range(80, 161):
            for j in range(100, 221):
                if pred[i][j] < 0.824:
                    status = 'stop'
                    break
    
        c.sendto(status.encode(), (host_ip, host_port))
		#cv2.imshow("test", pred)
        #cv2.imshow("webcam", frame)
        #fig = plt.figure()
        #ii = plt.imshow(pred, interpolation='nearest')
        #fig.colorbar(ii)
        #plt.show()
        #plt.pause(0.5)
        #break ## 나중에 없애야 함
	
        k = cv2.waitKey(1)
        if k == 27:
            break
    c.close()
    cap.release()
    cv2.destroyAllWindows()
    # Predict the image
    
    os._exit(0)

if __name__ == '__main__':
    main()

        



