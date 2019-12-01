#pip install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask flask-sqlalchemy
from flask import *

#import firebase4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


#execfile("firebase4.py")
