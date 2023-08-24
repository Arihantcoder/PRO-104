import cv2

image=cv2.imread("solar-system.jpg")
mytext="SUN"
cv2.putText(image,mytext,(100,100),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=5,color=(0,0,225))

mytext2="mercury"
cv2.putText(image,mytext2,(110,250),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(225,225,225))

mytext3="venus"
cv2.putText(image,mytext3,(200,250),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(225,225,225))

mytext4="earth"
cv2.putText(image,mytext4,(290,250),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(225,225,225))

mytext5="mars"
cv2.putText(image,mytext5,(380,250),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(225,225,225))

mytext6="jupiter"
cv2.putText(image,mytext6,(460,90),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=1,color=(225,225,225))

cv2.imshow('poster',image)
cv2.waitKey(0)