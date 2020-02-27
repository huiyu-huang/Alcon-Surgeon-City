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
from tensorflow.keras import backend
#from fpdf import FPDF



from database import upload, download, download2, download3

#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


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
value = "guest"
global folder
folder = 0

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
@app.route("/home")
def home():
    global value
    #make directory folder for the video
    try:
        os.makedirs("static/"+value)
        #os.rmdir("static/"+value)
    except:
        pass

    #textfile = open("storage/"+value +".txt","w+")
    #textfile.close()
    
    return render_template('sendvideo.html')

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


    #textfile = open("storage/"+value +".txt","w+")
    #textfile.close()
    
    return render_template('sendvideo2.html')

def fbeta(y_true, y_pred, beta=2):
	# clip predictions
	y_pred = backend.clip(y_pred, 0, 1)
	# calculate elements
	tp = backend.sum(backend.round(backend.clip(y_true * y_pred, 0, 1)), axis=1)
	fp = backend.sum(backend.round(backend.clip(y_pred - y_true, 0, 1)), axis=1)
	fn = backend.sum(backend.round(backend.clip(y_true - y_pred, 0, 1)), axis=1)
	# calculate precision
	p = tp / (tp + fp + backend.epsilon())
	# calculate recall
	r = tp / (tp + fn + backend.epsilon())
	# calculate fbeta, averaged across each class
	bb = beta ** 2
	fbeta_score = backend.mean((1 + bb) * (p * r) / (bb * p + r + backend.epsilon()))
	return fbeta_score

dependencies = {
     'fbeta': fbeta
}

model = load_model("model_v5.h5",custom_objects=dependencies)
def get_output(file):
  cap = cv2.VideoCapture(file)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH,400) #set properties of video ahead of time to correct dimensions
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
  fps = int(cap.get(5))
  sample_period = 10
  #time_series = [];
  output_matrix = []


  result = ""
  frame_count = 0
  while(cap.isOpened()):
    for i in range(sample_period): #capture every frame, or every 5 frames, based on sample_period
      ret, frame = cap.read()
      frame_count = frame_count + 1
      if (ret == False):
        break
   
    if ret == True: 
      
      frame = cv2.resize(frame,(400,400))
      frame = frame.astype(np.float32)
      img_tensor = np.expand_dims(frame, axis=0)
      img_tensor /= 255.

      pred = model.predict(img_tensor)
      pred = pred[0]
      threshold = .5
      label = ""

      for i in range(0,3):
          if (pred[i] > threshold):
              label = label + str(i) + "+"
      label = label[:-1]
      #time_series.append(label)
          
      
      result = result + "At time " + "{:.3f}".format(frame_count/fps) + " seconds detected tool "
      result = result + label + ","
      
      #cv2.imshow('frame',frame)

      #if cv2.waitKey(1) & 0xFF == ord('q'):
      #  break
   
    else:
      break 
   
  cap.release()

  #pie chart analysis goes here
  
  return result
   
  #cv2.destroyAllWindows()

#video result page, also done
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    global value
    global folder
    try:
        folder = folder+1
        os.makedirs("static/"+value +"/report" + str(folder)+"/video")
        os.makedirs("static/"+value +"/report" + str(folder)+"/image")
        #os.rmdir("static/"+value)
    except:
        pass
    # if there is a video in the file
    if 'photo' in request.files:
        #vid is the video stream
        vid = request.files['photo']
        if vid.filename != '':

            #vid.save(os.path.join(uploads_dir, value+'/' +vid.filename))

            #saves the video in the static folder as surgeryoutput.mp4
            vid.save(os.path.join(uploads_dir, value +"/report" + str(folder)+'/video'+'/surgeryoutput.mp4'))
            shutil.copy("static/" + value +"/report" + str(folder)+ "/video/"+ "surgeryoutput.mp4", "static/" + value +"/report" + str(folder)+ "/video/" + vid.filename)
            
            shutil.copy("static/" + "toolflow.jpg", "static/" + value +"/report" + str(folder)+ "/image/" + "toolflow.jpg")
            shutil.copy("static/" + "pygraph.jpg", "static/" + value +"/report" + str(folder)+ "/image/" + "pygraph.jpg")

            #duplicates the video


            #shortens the video if needed
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)

            #joshfile, will edit the video and saves it to the static folder as surgeryoutput.mp4
            #uploadvideo(vid.filename)

            outputstring = get_output("static/" + value + "/report" + str(folder)+"/video/" + vid.filename)

            #pic is already saved here

            
            #uploads the result video to the static folder to firebase
            upload("static/" +value+"/report" + str(folder)+"/video" +"/surgeryoutput.mp4")
            upload("static/" +value+"/report" + str(folder)+"/video/" + vid.filename)

            #image upload
            upload("static/" +value+"/report" + str(folder)+"/image/" + "toolflow.jpg")
            upload("static/" +value+"/report" + str(folder)+"/image/" + "pygraph.jpg")

            textfile = open("storage/"+value +".txt","a+")  
            textfile.close()
            
            #write the saved video into the txt file
            with open("storage/"+value +".txt", "r") as f:
                
               
                
                x = "static/" +value+"/" + vid.filename
                if x not in f.read():
                    textfile = open("storage/"+value +".txt","a+") 
                    textfile.write("static/" +value+"/report" + str(folder)+"/video/" + vid.filename + "\n")

##                    # text into pdf
##                    # save FPDF() class into  
##                    # a variable pdf 
##                    pdf = FPDF()    
##   
##                    # Add a page 
##                    pdf.add_page() 
##   
##                    # set style and size of font  
##                    # that you want in the pdf 
##                    pdf.set_font("Arial", size = 15)
##                    
##                    # insert the texts in pdf 
##                    for y in textfile: 
##                        pdf.cell(200, 10, txt = y, ln = 1, align = 'C') 
##   
##                    # save the pdf with name .pdf 
##                    pdf.output("storage/"+value +".pdf")
                    
                    textfile.close()
  
            

            #upload("test.txt")

            #downloads the video to the static folder from firebase
            download("static/"+value+"/report" + str(folder)+"/video" +"/surgeryoutput.mp4")

            #these two are redundent
            #download2("static/"+value+"/toolflow.jpg",value)
            #download3("static/"+value+"/pygraph.jpg",value)
            

            #this is to buffer the correct video
            time.sleep(5)

    return render_template('videoresult.html',output = outputstring)



#help page, will literally be text, no programs here
@app.route("/help")
def help():
    return render_template('help.html')


#uploaded video, can get videos back from here, list of video
@app.route("/myvideos")
def myvideos():
##    hists = os.listdir('static/plots')
##    hists = ['plots/' + file for file in hists]
    return render_template('myvideo.html')

@app.route("/myvideoresult")#, methods=['POST'])
def myvideoresult():
    return render_template('myvideoresult.html')


###I don't know what links is used for
@app.route("/links")
def links():
    return render_template('placeholder.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)       # run the flask app, don't use debug mode for non local demo
