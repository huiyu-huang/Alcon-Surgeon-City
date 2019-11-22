import pyrebase
import cv2

config = {
   # confidential
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# uploading mp4 file to Firebase Cloud Storage
#storage.child("eye_vids/new.mp4").put("small.mp4")

# downloading file from Cloud Storage
#storage.child("eye_vids/new.mp4").download("example.mp4")

# getting URL of the file when downloading (probably unnecessary)
# print(storage.child("images/new.mp4").get_url(None))

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
   if request.method == 'POST':
      upload = request.files['upload']
      storage.child("eye_vids/new.mp4").put(upload)

      # will be read by openCV
      storage.child("eye_vids/new.mp4").download("example.mp4")
      cap = cv2.VideoCapture('example.mp4');
      #while(True):
         #ret, frame = cap.read()
         #cv2.imshow('frame', frame)
         #if cv2.waitKey(1) & 0xFF == ord('q'):
            #break
      #cap.release()
      #cv2.destroyAllWindows()
   return render_template('index.html')

@app.route('/uploads')
def uploads():
   if request.method == 'POST':
      return redirect(url_for('basic'))
   if True:
      links = storage.child('eye_vids/new.mp4').get_url(None)
      return render_template('upload.html', l=links)
   return return_template('upload.html')

if __name__ == '__main__':
   app.run(debug = True)
