#-*-coding: utf-8 -*-
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

    #Default input size
    height = 480
    width = 640
    channels = 3
    batch_size = 1

    # Read image
    img = frame
    img = np.array(img).astype('float32')
    img = np.expand_dims(np.asarray(img), axis = 0)

    # Create a placeholder for the input image
    input_node = tf.placeholder(tf.float32, shape=(None, height, width, channels))

    # Construct the network
    net = models.ResNet50UpProj({'data' : input_node}, batch_size, 1, False)

    with tf.Session() as sess:

        # Load the converted parameters
        print('Loading the model')

        # Use to load from ckpt file
        saver = tf.train.Saver()
        saver.restore(sess, model_data_path)

        # Evaluate the network for the given image
        pred = sess.run(net.get_output(), feed_dict={input_node: img})
        tf.get_variable_scope().reuse_variables()

        return pred[0,:,:,0]

def main():
    # Parse arguments
    parser = arparse.ArgumentParser()
    parser.add_argument('model_path', help='Converted parameters for the model')
    args = parser.parse_args()

    path_dir = './GO/'
    file_list = os.listdir(path_dir)
    f = open('./go_test.txt', 'w')
    # Image
    for input in file_list:
        frame = Image.open(path_dir + input)
        pred = predict(args.model_path, frame)

        status = 'go'
        for i in range(80, 161):
            for j in range(100, 221):
                if pred[i][j] < 0.824:
                    status = 'stop'
                    break
        print(status)
        f.write(status + '\n')

    f.close()
    os.exit(0)

if __name__ == '__main__':
    main()
