from flask import Flask, request, render_template, url_for, redirect,jsonify
import os
app = Flask(__name__,static_folder='static')
value = "1"


@app.route('/')
def random():
    return "This needs to work"
@app.route('/upload',methods=['POST'])
def test():
    if 'video' in request.files:
        video=request.files['video']
        if video.filename != '':
            video.save(os.path.join('../public/uploads',video.filename))
        filename=video.filename
        path='../public/uploads/' +f'{video.filename}'
    return jsonify(fileName = filename,filePath=path)

    # if (request.method == "Post"):
    #     print('successfully communicated frontend and backend', file=sys.stderr)
    #     req=request.form
    #     file=req.file
    #     shutil.move(file, '../public/uploads'/file.name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)
