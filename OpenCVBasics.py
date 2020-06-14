import cv2 #loading opencv library into python code

img=cv2.imread("Samples/flower.jpg")

#print(img[100][100]) #printing a specific RGB(GBR) colour in a selected pixel

#img[100][100]=[255,255,255] #assign a color to a pixel

#cv2.rectangle(img,(100,100),(200,200),(0,255,0),2) #image name,starting point,end point,line colour(BGR),line width(in pixles)

#cv2.circle(img,(150,150),40,(0,0,255),-1) #image name,center point,radius,line colour,line width in pixels
# use minus value as line width (-1) will result a filled circle/rectangle

cv2.imshow("WINDOW",img) #showing the actual image in a seperate window

