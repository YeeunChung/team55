## setup logging
#import logging
#logging.basicConfig(level = logging.INFO)

## import the package
import pyrealsense as pyrs
from pyrealsense.constants import rs_option
import cv2
import numpy as np

def convert_z16_to_bgr(frame):
  '''Performs depth histogram normalization
  This raw Python implementation is slow. See here for a fast implementation using Cython:
  https://github.com/pupil-labs/pupil/blob/master/pupil_src/shared_modules/cython_methods/methods.pyx
  '''
  hist = np.histogram(frame, bins=0x10000)[0]
  hist = np.cumsum(hist)
  hist -= hist[0]
  rgb_frame = np.empty(frame.shape[:2] + (3,), dtype=np.uint8)

  zeros = frame == 0
  non_zeros = frame != 0

  f = hist[frame[non_zeros]] * 255 / (hist[0xFFFF])
  rgb_frame[non_zeros, 0] = 255 - f
  rgb_frame[non_zeros, 1] = 255 - f
  rgb_frame[non_zeros, 2] = 255 - f
  rgb_frame[zeros, 0] = 20
  rgb_frame[zeros, 1] = 5
  rgb_frame[zeros, 2] = 0
  return rgb_frame

 

## main code

color_stream = pyrs.stream.ColorStream(fps=60)
depth_stream = pyrs.stream.DepthStream(fps=60)
## start the service - also available as context manager
serv = pyrs.Service()

## create a device from device id and streams of interest
cam = serv.Device(device_id = 0, streams = [color_stream, depth_stream])

## retrieve 60 frames of data
cnt = 0
num = 0
while True:
  try:
    cnt += 1
    cam.wait_for_frames()
    c = cam.color
    c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)
#    d = cam.depth * cam.depth_scale * 1000
#    d = cv2.applyColorMap(d.astype(np.uint8), cv2.COLORMAP_RAINBOW)
    d = cam.depth
    d = convert_z16_to_bgr(d)

    cd = np.concatenate((c, d), axis=1)
    cv2.imshow('', cd)
    if cnt % 10 == 0:
	num += 1
        cv2.imwrite('./save/c/c'+str(num)+'.jpg', c)
    	cv2.imwrite('./save/d/d'+str(num)+'.png', d)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break;
  except:
    print('internal error')
    break;

## stop camera and service
cam.stop()
serv.stop()
