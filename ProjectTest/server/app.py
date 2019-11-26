from database import *
import os
import sys
from database import upload
from audioRead import audio_read
# app.py
from flask import Flask, request, render_template, url_for, redirect          # import flask
app = Flask(__name__,static_folder='static')             # create an app instance


@app.route("/")                   # at the end point /
def start():                      # call method hello
    #return "Hello World!"         # which returns "hello world"
    return render_template('fireform.html')

@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        vid = request.files['photo']
        if vid.filename != '':
            audio_read(vid.filename)
            upload(vid.filename)
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server', vid.filename))
            vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename))
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/templates', vid.filename))
            #upload(vid.filename)
    return render_template('video.html') #redirect('/') #return report



if __name__ == "__main__":        # on running python app.py
    #upload()
    app.run(host='127.0.0.1',debug=True)                     # run the flask app

