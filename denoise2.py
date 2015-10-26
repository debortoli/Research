import numpy as np
import cv2
import time
cap = cv2.VideoCapture('hallsmooth17.mp4')
#think about setting the frame height and width before the processing
out = cv2.VideoWriter('output4.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 20.0, (360,288))

while(True):
    ret, frame = cap.read()
    median = cv2.medianBlur(frame,5)
    dst = cv2.fastNlMeansDenoisingMulti(median, 2, 5, None, 4, 7, 35)
    cv2.imshow('frame',dst)
    out.write(dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()