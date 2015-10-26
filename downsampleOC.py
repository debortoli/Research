import numpy as np
import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('noisyImage.png')
print "Hi"
dst = cv2.pyrDown(img,None)
cv2.imwrite('down.mpg',dst)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()