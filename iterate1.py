import cv2
img=cv2.imread('noisyImage.png')
average_r=0
average_g=0
average_b=0

height = 84
width=84
for w in xrange(1,5):
	height += 50
	width += 50
	average_r=0
	average_g=0
	average_b=0
	for i in xrange(height-50,height):
		for j in xrange(width-50,width):
			r, g, b = img[i,j]
			average_r+=r
			average_g+=g
			average_b+=b
			# if(j==99):
			# 	print '\n'
			# 	print '---------------------------------------------'
			# print r, g, b, "|||",
	average_r=average_r/(50*50)
	average_g=average_g/(50*50)
	average_b=average_b/(50*50)
	# if (average_b>120)or(average_r>120)or(average_g>120) :
	# 	print "Bad"
	# else:
	# 	print "Good"
	print average_r, average_g, average_b
	cropped = img[height-50:height, width-50:width]
	cv2.imshow("cropped", cropped)
	cv2.waitKey(0)