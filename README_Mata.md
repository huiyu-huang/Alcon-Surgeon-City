import numpy as np
import cv2

cap = cv2.VideoCapture('SampleVideo_1280x720_1mb.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

// I found that we could use the openCV library in python to handle the image
// and video processing.
// This code takes in a video as inout and shows it to you frame by frame
// We can manipulate this and work on each frame at a time and check if each
// frame contains a key image that we want to identify such as a tool used
// in surgery.
// To do this identifying we need to use machine learning to train a program to
//  identify the images and flag them so that we can save them for the
// highlight of the surgery.

// I also looked into how to implement machine learning. There are many
// libraries and established networks whose code we can use as reference, but
//  the greater challenge that we faced that I noticed from the research that
// I did was that we need a good set of training data to put into our machine
// learning algorithm, which we don't have. This is going to be a one of our
// greater challenges since we do not have a bunch of images of eye surgery
// tools to use to train the data.

// The following is some example code of how we can train a program ourselves
// once we have a good training data set

function traindata()
Birds=zeros(36,5);
myFolder='Birds';
if ~isdir(myFolder)
  errorMessage = sprintf('Error: The following folder does not exist:\n%s', myFolder);
  uiwait(warndlg(errorMessage));
  return;
end
filepattern=fullfile(myFolder,'*.wav');
Files=dir(filepattern);
numel(Files);
Files(2);
for i=1:numel(Files)
    filename=Files(i).name;
    fullname=fullfile(myFolder,filename);
    [aud,fs]=audioread(fullname);
    feat=features(aud,fs);
    Birds(i,:)=feat(1,:);
