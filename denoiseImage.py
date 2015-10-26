import numpy as np
import cv2
from matplotlib import pyplot as plt
import resource
 
img = cv2.imread('noisyImage.png')
img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print "Hi"
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss