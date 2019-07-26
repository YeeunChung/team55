## setup logging
#import logging
#logging.basicConfig(level = logging.INFO)

## import the package
import pyrealsense as pyrs
from pyrealsense.constants import rs_option
import cv2
import numpy as np



def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
	global global_x, global_y
        global_x, global_y = x, y
        print('x, y = ', global_x, global_y)
	

## main code

global_x = 0
global_y = 0
color_stream = pyrs.stream.ColorStream(fps=60)
depth_stream = pyrs.stream.DepthStream(fps=60)
DAC_stream = pyrs.stream.DACStream(fps=60)
## start the service - also available as context manager
serv = pyrs.Service()

## create a device from device id and streams of interest
cam = serv.Device(device_id = 0, streams = [color_stream, depth_stream, DAC_stream])

## retrieve 60 frames of data
cnt = 0
num = 101474

#scale = cam.depth_scale*1000*255/2800
scale = cam.depth_scale*1000
print('scale = ', scale)
print('depth scale = ', cam.depth_scale)

while True:
  
    cnt += 1
    cam.wait_for_frames()
    c = cam.color
    c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
   
    #d = cam.dac
    d = cam.dac * scale
    #d = d.astype(np.uint8)
    #d = cv2.applyColorMap(d.astype(np.uint8), cv2.COLOR_RGB2GRAY)
    
    #d = cam.dac
    
    #d = convert_z16_to_bgr(d)
   
    #cd = np.concatenate((c, d), axis=1)
    #cv2.imshow('', cd)
    cv2.imshow('c', c)
    cv2.imshow('d', d)
    cv2.setMouseCallback('d', mouse_callback)
    if cnt % 60 == 0:
	num += 1
        cv2.imwrite('./save0712/c/c'+str(num)+'.jpg', c)
    	cv2.imwrite('./save0712/d/d'+str(num)+'.png', d)
	print('x, y = ', global_x, global_y)
	print(d[global_x,global_y])
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break;
  
## stop camera and service
cam.stop()
serv.stop()
