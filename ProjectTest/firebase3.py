import firebase_admin
from firebase_admin import credentials, firestore, storage

cred=credentials.Certificate('acc.json') #credentials, don't know if needed
firebase_admin.initialize_app(cred, {
    'storageBucket': 'meprojec.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()
blob = bucket.blob('shia2.mp4') #what the file name will be called on firebase
outfile='shia.mp4' #what file you want to upload to firebase
blob.upload_from_filename(outfile)
