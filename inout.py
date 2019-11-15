import numpy as np
import cv2
import sys

def detectObject(im):
	"""Gets the coordinates of a box around an object and accuracy of an object
	im is the frame you pass"""

	#stub

	ul = (np.random.randint(0,im.shape[0]+1),np.random.randint(0,im.shape[1]+1)) #upper-left corner
	lr = (np.random.randint(ul[0],im.shape[0]+1),np.random.randint(ul[1],im.shape[1]+1)) #lower-right corner
	accuracy = np.round(np.random.uniform(0,100),2)
	return ul,lr,accuracy

def drawBox(im,ul,lr,accuracy):
	"""Draws a box around object with accuracy label"""
	im = cv2.rectangle(im,ul,lr,(0,0,255),5)
	#ret, baseLine = cv2.getTextSize(str(accuracy),cv2.FONT_HERSHEY_PLAIN,1,1)
	#y = ul[0]-ret[1] if ul[0]-ret[1] > 0 else ul[0]
	#im = cv2.rectangle(im,(y,ul[1]),(ul[1]+ret[0],ul[0]),(0,0,255),-1)
	im = cv2.putText(im,str(accuracy),ul,cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1,lineType = cv2.LINE_AA);

def showImage(im):
	cv2.imshow('Frame',im)
	if cv2.waitKey(0) & 0xFF == ord('q'):
		cv2.destroyAllWindows()

if __name__ == "__main__":
	if len(sys.argv) == 2:
		cap = cv2.VideoCapture(sys.argv[1])
		width = int(cap.get(3))
		height = int(cap.get(4))
		fps = int(cap.get(5))
		fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
		out = cv2.VideoWriter('output.avi', fourcc, fps, (width,height))
		i = 10
		while (cap.isOpened()):
			ret, frame = cap.read()
			if ret == True:
				if i == 10:
					ul,lr,accuracy = detectObject(frame)
					#drawBox(frame,ul,lr,accuracy)
					out.write(frame)
					#showImage(frame)
					i = 1
					continue
			else:
				break
			i = i + 1

		cap.release()
		out.release()
		cv2.destroyAllWindows()

