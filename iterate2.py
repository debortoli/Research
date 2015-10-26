import cv2
img=cv2.imread('noisyImage.png')
average_r=0
average_g=0
average_b=0
average_diff=0

height = 84
width=84
for w in xrange(1,5):
	height += 100
	width += 100
	average_diff=0
	for i in xrange(height-100,height):
		for j in xrange(width-100,width):
			r, g, b = img[i,j]
			r2,g2,b2=img[i+1,j+1]
			average_diff+=((r2-r)+(g2-g)+(b2-b))/3
			# if(j==99):
			# 	print '\n'
			# 	print '---------------------------------------------'
			# print r, g, b, "|||",
	average_diff/(100*100)
	# if (average_b>120)or(average_r>120)or(average_g>120) :
	# 	print "Bad"
	# else:
	# 	print "Good"
	print average_diff
	cropped = img[height-100:height, width-100:width]
	cv2.imshow("cropped", cropped)
	cv2.waitKey(0)