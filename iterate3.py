from PIL import Image
import numpy as np
from numpy import *
from pylab import *
from PIL import *
from scipy import signal as sg

im = Image.open("noisyImage.png")
def estimate_noise(I):

  H=I.size[1]
  W=I.size[0]

  M = [[1, -2, 1],
       [-2, 4, -2],
       [1, -2, 1]]

  sigma = np.sum(np.sum(np.absolute(convolve2d(I, M))))
  sigma = sigma * math.sqrt(0.5 * math.pi) / (6 * (W-2) * (H-2))
  print sigma
  return sigma
# print img
estimate_noise(im)