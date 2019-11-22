#chris and I were trying to figure out how to upload and download from firebase
#the difference is that I'm trying to put the video in a data stream object
#instead of downloading the file then opening it so I can use it for OpenCV

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os

def init():
	cred = credentials.Certificate('serviceaccountkey.json')
	firebase_admin.initialize_app(cred, {
	    'storageBucket': 'test-b3333.appspot.com'
	})
	return cred

def download_blob(download = False):
	bucket = storage.bucket()
	blob = bucket.get_blob('surgery1.mp4')
	if download:
		with open("blob.mp4", "wb") as file_obj:
	   		blob.download_to_file(file_obj)
	return blob

def download_bucket():
	bucket = storage.bucket()
	return bucket

def getStream(blob):
    stream = open('myStream.mp4','wb', os.O_NONBLOCK)
    streaming = blob.download_to_file(stream)
    return streaming