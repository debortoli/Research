import numpy as np
from numpy import *
import cv2
import time
cap = cv2.VideoCapture('hall10.mp4')
#think about setting the frame height and width before the processing
out = cv2.VideoWriter('output5.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (720,576))
good_count=0
bad_count=0
while(True):
    try:
        ret, frame = cap.read()
        #dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
    	#dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
        img=frame
        average_r=0
        average_g=0
        average_b=0

        big_avgr=zeros(5)
        big_avgg=zeros(5)
        big_avgb=zeros(5)

        good=True
        heights=array([100,200,300,400,500])
        width=3
        threshold=13

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
                    #   print '\n'
                    #   print '---------------------------------------------'
                    # print r, g, b, "|||",
            average_r=average_r/(100*width)
            average_g=average_g/(100*width)
            average_b=average_b/(100*width)
            # if (average_b>120)or(average_r>120)or(average_g>120) :
            #   print "Bad"
            # else:
            #   print "Good"
            if(average_r)>threshold:
                print average_r
                good=False
            if(average_g)>threshold:
                print average_g
                good=False
            if(average_b)>threshold:
                print average_b
                good=False
        
        if good:
            print "GOOD"
            cv2.imshow("image", img)
            out.write(img)
            good_count+=1
        else:
            print "BAD"
            bad_count+=1
            #cv2.imshow("image", img)
            #time.sleep(2.5)
    
    except:
        print "------End------" 
        break   

    
        #cropped = img[heights[k]-100:heights[k], 0:width]
    #cv2.imshow("image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# When everything done, release the capture
#resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print "Good frames: ",good_count, "---",round(good_count*100./(good_count+bad_count),3),"%"
print "Bad frames:  ",bad_count,  "---",round(bad_count*100./(good_count+bad_count),3),"%"
cap.release()
cv2.destroyAllWindows()