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
