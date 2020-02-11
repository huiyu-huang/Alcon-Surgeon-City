from database import *
import os
import sys
import time
import shutil
import pyrebase
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image



from database import upload, download

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


#import moviepy.editor as mp
#from joshfile import uploadvideo

from flask import *
#Flask, request, render_template, url_for, redirect
#from audioRead import audio_read
#import numpy as np
app = Flask(__name__,static_folder='static')


#config thing
config = {
  # confidential
  "apiKey": "AIzaSyBfJeaQjeU2q_g1zaC_rvJ2D2jEDq58umI",
  "authDomain": "eyelight-vids.firebaseapp.com",
  "databaseURL": "https://eyelight-vids.firebaseio.com",
  "projectId": "eyelight-vids",
  "storageBucket": "eyelight-vids.appspot.com",
  "messagingSenderId": "359657414936",
  "appId": "1:359657414936:web:f24f7ad0acd3a27a2afe6d",
  "measurementId": "G-RHHY80M6DP"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


#value is the id
global value
value = "1"

#line below is for place to save video
uploads_dir = os.path.join(app.root_path, 'static')

##@app.route("/", methods=['GET', 'POST'])
##def my_index():
##    return render_template("index.html",token="Hello Flask+react")

#home page, will be the login/signup page
@app.route("/", methods=['GET', 'POST'])
def login():
    global value
    unsuccessful = 'Incorrect email or password entered'
    successful = 'Login successful'
    if request.method == 'POST':
	    email = request.form['name']
	    password = request.form['pass']
	    try:
		    auth.sign_in_with_email_and_password(email, password)
		    value = email
		    return redirect(url_for('uploader')) # I believe this should be the correct "linking" line
		    # return render_template('login.html', s=successful) # replaced
	    except:
		    return render_template('login.html', us=unsuccessful)

    return render_template('login.html')

#logoff page
@app.route("/logoff")
def logoff():
    #return redirect(url_for('login')), if not logged in

    return render_template('placeholder.html')

#account setting?
@app.route("/deleteaccount")
def deleteaccount():
    #return redirect(url_for('login')), if not logged in

    return render_template('placeholder.html')


#upload page, already done
@app.route("/upload")
def uploader():
    global value
    #make directory folder for the video
    try:
        os.makedirs("static/"+value)
        #os.rmdir("static/"+value)
    except:
        pass
    return render_template('sendvideo.html')

def get_output(file):
  cap = cv2.VideoCapture("surgery1clip.mp4")
  cap.set(cv2.CAP_PROP_FRAME_WIDTH,224) #set properties of video ahead of time to correct dimensions
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT,224)
  fps = int(cap.get(5))
  sample_period = 10

  model = load_model("my_model.h5")

  result = ""
  frame_count = 0
  while(cap.isOpened()):
    for i in range(sample_period): #capture every frame, or every 5 frames, based on sample_period
      ret, frame = cap.read()
      frame_count = frame_count + 1
      if (ret == False):
        break
   
    if ret == True: 
      
      frame = cv2.resize(frame,(224,224))
      frame = frame.astype(np.float32)
      img_tensor = np.expand_dims(frame, axis=0)
      img_tensor /= 255.

      pred = model.predict(img_tensor)

      result = result + "At time " + "{:.3f}".format(frame_count/fps) + " seconds detected tool "
      result = result + str(np.argmax(pred)) + ","
      
      #cv2.imshow('frame',frame)

      #if cv2.waitKey(1) & 0xFF == ord('q'):
      #  break
   
    else:
      break 
   
  cap.release()
  return result
   
  #cv2.destroyAllWindows()

#video result page, also done
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    global value
    # if there is a video in the file
    if 'photo' in request.files:
        #vid is the video stream
        vid = request.files['photo']
        if vid.filename != '':

            #vid.save(os.path.join(uploads_dir, value+'/' +vid.filename))

            #saves the video in the static folder as surgeryoutput.mp4
            vid.save(os.path.join(uploads_dir, value+'/surgeryoutput.mp4'))
            shutil.copy("static/" + value + "/surgeryoutput.mp4", "static/" + value + "/" + vid.filename)

            #duplicates the video

            #ffmpeg alert
            #cut()
            #ffmpeg_extract_subclip("static/" + value + "/" + vid.filename, 0, 10, targetname="static/" + value + "/surgeryoutput.mp4")
            

            #shortens the video if needed
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)

            #joshfile, will edit the video and saves it to the static folder as surgeryoutput.mp4
            #uploadvideo(vid.filename)

            outputstring = get_output("static/" + value + "/" + vid.filename)
            #uploads the result video to the static folder to firebase
            upload("static/" +value+"/surgeryoutput.mp4")
            upload("static/" +value+"/" + vid.filename)

            #upload("test.txt")

            #downloads the video to the static folder from firebase
            download("static/"+value+"/surgeryoutput.mp4")

            #this is to buffer the correct video
            time.sleep(5)

    return render_template('videoresult.html',output = outputstring)



#help page, will literally be text, no programs here
@app.route("/help")
def help():
    return render_template('placeholder.html')


#uploaded video, can get videos back from here, list of video
@app.route("/myvideo")
def myvideo():
    return render_template('placeholder.html')


###I don't know what links is used for
@app.route("/links")
def links():
    return render_template('placeholder.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)       # run the flask app, don't use debug mode for non local demo
