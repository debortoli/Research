import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import pylab

time1=time.time()
img = cv2.imread('noisyImage.png')
median = cv2.medianBlur(img,7)
#dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
#dst = cv2.fastNlMeansDenoising(median,None,3,7,21)
print time.time()-time1


plt.subplot(211),plt.imshow(img)
#plt.subplot(3,1,2),plt.imshow(dst)
plt.subplot(212),plt.imshow(median)

plt.show()