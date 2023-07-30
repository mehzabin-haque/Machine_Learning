from PIL import Image
import os
import glob
import time
import numpy as NP

start_time = time.time()

skin_pix_count = NP.zeros([256,256,256])
non_skin_pix_count = NP.zeros([256,256,256])
probability_skin = NP.zeros([256,256,256])
probability_non_skin = NP.zeros([256,256,256])
total_skin = 0
total_non_skin = 0 



images = sorted(glob.glob('F:\DBMS-II\ibtd\*.jpg'))
masks = sorted(glob.glob('F:\DBMS-II\ibtd\Mask\*.bmp'))

file = open('datas.txt', 'w')

for i in range (0, len(images)):
    img = Image.open(images[i])
    mask = Image.open(masks[i])
    #pixel_img = img.load()
    #pixel_mask = mask.load()

    for (pixel, pix_mask) in zip(img.getdata(), mask.getdata()):
        
        if pix_mask[0] < 255 or pix_mask[1] < 255 or pix_mask[2] < 255:
            skin_pix_count[pixel[0]][pixel[1]][pixel[2]] += 1
            total_skin += 1
        else:
            non_skin_pix_count[pixel[0]][pixel[1]][pixel[2]] += 1
            total_non_skin += 1


for i in range (0, 256):
    for j in range (0, 256):
        for k in range (0, 256):
            probability_skin[i][j][k] = skin_pix_count[i][j][k]/total_skin
            probability_non_skin[i][j][k] = non_skin_pix_count[i][j][k]/total_non_skin
            if probability_non_skin[i][j][k] == 0 and probability_skin[i][j][k] == 0:
                file.write(str(0)+"\n")
            elif probability_non_skin[i][j][k] == 0:
                file.write(str(100)+"\n")
            else:
                probability_skin[i][j][k] = probability_skin[i][j][k]/probability_non_skin[i][j][k]
                #print(probability_skin[i][j][k])
                file.write(str(probability_skin[i][j][k])+"\n")
file.close()
end_time = time.time()
print(end_time-start_time)
