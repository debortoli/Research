import numpy as np
import cv2
import time
cap = cv2.VideoCapture('hallsmooth17.mp4')
#think about setting the frame height and width before the processing
out = cv2.VideoWriter('output5.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (720,576))

while(True):
    ret, frame = cap.read()
    median = cv2.medianBlur(frame,9)
    #dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
	#dst = cv2.fastNlMeansDenoisingColored(median,None,10,10,7,21)
    cv2.imshow('frame',median)
    # width, height = median.shape[:2]
    # print width, height
    out.write(median)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# When everything done, release the capture
resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
cap.release()
cv2.destroyAllWindows()