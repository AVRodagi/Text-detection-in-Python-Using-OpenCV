#import necessary modules
import cv2
#read the input image
img = cv2.imread("kannada.png")
#convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('g.png',gray)
#set threshold to converted image
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
cv2.imwrite('black.png',thresh1)
#threshold=0; max=255; thresholding techniques used are otsu and binary_inv,resulting tuples values are concatenated
#| character can also be used in place of + to concatenate two tuples
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
#smaller the kernel size more precise the detection is going to be
#dialting the text in image, expanding the text area; making it more detectable
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
#input image;rectangular kernel;number of times the dilation is applied;src;kernel;iteration
#applying contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#approx:all the boundary values;retr: return only outer extreme flags
im2 = img.copy()
#copy image 
#applying rectangular structures
for cnt in contours:
	x, y, w, h = cv2.boundingRect(cnt)
	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255,0), 2)
 	#image;coordinate;rectangle;BGR color;thickness of rectangle
	cv2.imwrite('ss.jpg',im2)