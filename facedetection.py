import cv2
#creating object for CascadeClassifier
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#creating object for Image
img=cv2.imread("Image.jpg")
#converting to gray
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#finding face 
faces=face.detectMultiScale(g,scaleFactor=1.05,minNeighbors=5)
#print face cooridnates
print (faces)
#creating rectangle in image
for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
resized=cv2.resize(img,(600,600))
cv2.imshow("Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
