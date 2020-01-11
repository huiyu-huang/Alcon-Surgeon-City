import firebase_admin
from firebase_admin import credentials, firestore, storage


count = 0

#uploads to video to firebase
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

#downloads the video from firebase
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
    blob = bucket.blob('static/surgeryoutput.mp4') #what the file name will be called on firebase

    #what file it will be called, will be a temporary file
    with open("harvard.mp4", "wb") as file_obj:
        blob.download_to_file(file_obj)

