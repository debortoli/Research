import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noisyImage.png')
# img_bw = 255*(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) > 5).astype('uint8')

# se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
# mask = cv2.morphologyEx(img_bw, cv2.MORPH_CLOSE, se1)
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)

# mask = np.dstack([mask, mask, mask]) / 255
# out = img * mask

median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(median)
plt.show()