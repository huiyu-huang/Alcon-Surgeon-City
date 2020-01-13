# Met with mentors on 01/09

# Mentors suggested either using Flask or AWS for hosting
# in order to allow users to access the stored videos

# After researching, I determined that Flask may be easier to use.
# It appears that both Flask and AWS offer the necessary functionalities
# for this project.
# However, AWS is known to be more difficult to learn.

# Now we are consulting the internet for help on hosting:

# this code will be under the diretory server/src

from flask import Flask, render_template, make_response
import os
import time

app = Flask(__name__)

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route('/')
def index():
    context = { 'server_time': format_server_time() }

    #the next few lines allows us to control how long content (video
    # in this case) can be stored in Firebase's Content Delivery Network (CDN)
    # optional probably
    template = render_template('index.html', context=context)
    response = make_response(template)
    response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'

    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
