import firebase_admin
from firebase_admin import credentials, firestore, storage

cred=credentials.Certificate('acc.json') #credentials, don't know if needed
firebase_admin.initialize_app(cred, {
    'storageBucket': 'meprojec.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()
blob = bucket.blob('static/surgeryoutput.mp4') #what the file name is called on firebase

#outfile='TEST.txt' #what file you want to upload to firebase

#how to download files from firebase
with open("harvard.mp4", "wb") as file_obj:
    blob.download_to_file(file_obj)
