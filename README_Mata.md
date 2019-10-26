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
    
    --------------------------------------------------------------------------------
10/25/19

This week we worked to redefine our project idea. One of the things that
we decided that we were going to need a web app for our project is that. I have
previously worked on a web app, however I only worked on the backend of the
project.

For this project I am going to be tasked with working on the front end of the
web app. I don't have a lot of experience with working on front end programming,
including the languages.

I have began to do some research on how making a web app works and will put in
the time to do the work

I have also recently started doing an online course on Udemy for web development
This will be a good opportunity to learn and get better at new skills
and apply some of the things that I learned through the online course.

Much of the work that we did this week was on continuing the research we did on
machine learning. And again it went into looking into our project and improving
it, so that is more clearly defined. We met with our mentors to work on a new
idea for the project, and got some good input form them.

This week I also looked into last years PRDs to get a better idea of what is
expected from the document. I got a better understanding of what we need to do
and the main ideas. All the documents had an intro, a high level diagram of the
project idea, a list of the user stories, and a lost of the technologies that
were going to be used. 
