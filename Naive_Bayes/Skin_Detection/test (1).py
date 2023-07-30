from cgi import test
from PIL import Image
import os
import glob
from cmath import pi
import numpy as NP

probability = NP.zeros([256,256,256])
f = open('datas.txt', 'r')
threshold = 1.0
count=0
for i in range (0, 256):
    for j in range (0, 256):
        for k in range (0, 256):
            line = f.readline()             
            probability[i][j][k] = float(line)
            
testImage = Image.open("iputImage.jpg")
pixel = testImage.load()
pixel_out = testImage.load()

for y in range (0, testImage.size[1]):
    for x in range (0,testImage.size[0]):
        if probability[pixel[x,y][0]][pixel[x,y][1]][pixel[x,y][2]] >= threshold:
            pixel_out[x,y] = pixel[x,y]
        else:
            pixel_out[x,y] = (255,255,255)
testImage.save("outputImage.bmp")





