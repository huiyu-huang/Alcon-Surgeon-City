from database import *
import os
import sys
import time
import shutil
from database import upload, download

import moviepy.editor as mp
#from joshfile import uploadvideo

from flask import Flask, request, render_template, url_for, redirect
#from audioRead import audio_read
#import numpy as np
app = Flask(__name__,static_folder='static')

#value is the id
value = "1"



#line below is for place to save video
uploads_dir = os.path.join(app.root_path, 'static')

#home page, will be the login/signup page
@app.route("/")                   
def start():
    
    #make directory folder for the video
    try:
        os.makedirs("static/"+value)
        #os.rmdir("static/"+value)
    except:
        pass
    return render_template('sendvideo.html')

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
    return render_template('sendvideo.html')

#video result page, also done
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
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
            
            

            #shortens the video if needed
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)

            #joshfile, will edit the video and saves it to the static folder as surgeryoutput.mp4
            #uploadvideo(vid.filename)

            #uploads the result video to the static folder to firebase
            upload("static/" +value+"/surgeryoutput.mp4")
            upload("static/" +value+"/" + vid.filename)

            #upload("test.txt")

            #downloads the video to the static folder from firebase
            download("static/"+value+"/surgeryoutput.mp4")

            #this is to buffer the correct video
            time.sleep(5)

    return render_template('videoresult.html')


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

