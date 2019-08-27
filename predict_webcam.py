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
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', help='Converted parameters for the model')
    parser.add_argument('image_paths', help='Directory of images to predict')
    args = parser.parse_args()
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    while True:
        print(1)
        ret, frame = cap.read()
        pred = predict(args.model_path, frame)
        
        flag = 0
        for i in range(80, 161):
            for j in range(100, 221):
                if pred[i][j] < 0.824:
                    flag = 1
                    break
    
        print(flag)
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
    cap.release()
    cv2.destroyAllWindows()
    # Predict the image
    #pred = predict(args.model_path, )
    
    os._exit(0)

if __name__ == '__main__':
    main()

        



