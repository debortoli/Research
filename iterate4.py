import cv2
import numpy
from numpy import *
img=cv2.imread('badScreenshot.png')
average_r=0
average_g=0
average_b=0

heights=array([100,200,300,400,500])
width=5
#print img.shape
average_r=0
average_g=0
average_b=0
for k in xrange(0,5):
	average_r=0
	average_g=0
	average_b=0
	for i in xrange(heights[k]-100,heights[k]):
		for j in xrange(width):
			r, g, b = img[i,j]
			average_r+=r
			average_g+=g
			average_b+=b
			# if(j==99):
			# 	print '\n'
			# 	print '---------------------------------------------'
			# print r, g, b, "|||",
	average_r=average_r/(100*width)
	average_g=average_g/(100*width)
	average_b=average_b/(100*width)
	# if (average_b>120)or(average_r>120)or(average_g>120) :
	# 	print "Bad"
	# else:
	# 	print "Good"
	print average_r, average_g, average_b
	cropped = img[heights[k]-100:heights[k], 0:width]
	cv2.imshow("cropped", cropped)
	cv2.waitKey(0)