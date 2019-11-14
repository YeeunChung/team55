
# coding: utf-8

# In[ ]:


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

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
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
        
        while True:
            ret, frame = cap.read()
            cv2.imshow("webcam", frame)

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
                        break
            print(status)
            
            k = cv2.waitKey(1)
            if k == 27:
                break
            
        cap.release()
        cv2.destroyAllWindows()
    os._exit(0)

if __name__ == '__main__':
    main()

