from flask import Flask, request, render_template, url_for, redirect,jsonify
import os
import time
import firebase_admin
from firebase_admin import credentials, firestore, storage
count = 0
def upload(video):
    global count
    if  count == 0:
        cred=credentials.Certificate('acc.json') #credentials, don't know if needed
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'meprojec.appspot.com'
        })
        count += 1

    db = firestore.client()
    bucket = storage.bucket()
    blob = bucket.blob(video) #what the file name will be called on firebase
    outfile=video #what file you want to upload to firebase

    #how to upload file
    blob.upload_from_filename(outfile)


def download(video):
    global count
    if  count == 0:
        cred=credentials.Certificate('acc.json') #credentials, don't know if needed
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'meprojec.appspot.com'
        })
        count += 1

    db = firestore.client()
    bucket = storage.bucket()
    blob = bucket.blob(video) #what the file name will be called on firebase
    print(blob.public_url)
    return (blob.public_url)
    #how to upload file
    # with open("../public/download/output.mp4", "wb") as file_obj:
    #     blob.download_to_file(file_obj)
app = Flask(__name__,static_folder='static')
value = "1"
temp=False
path=''
@app.route('/')
def random():
    return "This needs to work"
@app.route('/upload',methods=['POST'])
def test():
    global path
    if 'video' in request.files:
        video=request.files['video']
        if video.filename != '':
            video.save(os.path.join('../public/uploads',video.filename))
        filename=video.filename
        path ='../public/uploads/' + f'{video.filename}'
        temp=True
        if(temp):
            print("hello world")
            temp=False
        upload(path)
        upload('../src/assets/pie_chart.jpg')
        upload('../src/assets/graph.jpg')
        print(path)
    return jsonify(fileName = filename,filePath=path)
@app.route('/watch',methods=['GET'])
def fire():
    global path
    if request.method == "GET":
        print ("finally")
    print ("still here")
    time.sleep(5)
    stuff=download(path)
    pie_chart=download('../src/assets/pie_chart.jpg')
    graph=download('../src/assests/graph.jpg')
    return jsonify(info = stuff, info1=pie_chart,info2 = graph)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
