import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "sayan.jpeg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    # it is 2D array formulla to convert image to grayscale

def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    # if image is greater than 255 which i dont think is possible but stil we can do it
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    # to convert any suitable existing coloumn to categorical type we will use aspecet function
    # and unit 8 is for 8-bit signed integer
    return final_sketch.astype('uint8')    

ss = imageio.imread(img)
gray = rgb2gray(ss) # convert to grayscale

i = 255 - gray # 0,0,0 is for darkest color and 255,255,255 is for brightest color

# to convert it into blur image
blur = scipy.ndimage.gaussian_filter(i, sigma=200)
# sigma is the intensity of the blur
r = dodge(blur,gray) # this function will convet our image to sketch by taking two parameter as blur and gray


cv2.imwrite("Sketch.png", r)