The directory path you are in right now is the root

Before: pip3 install -r requirements.txt ( install programs in requirements)
pip freeze > requirements.txt (in case of updates, list the programs into the requirements.txt)
1. python app.py or double click app.py. This opens up the localhost server at http://localhost:5000/.
2. Go to http://localhost:5000/ . You will see the homepage from the code in templates/sendvideo.html
3. Insert a .mp4 file only and click submit
4. It should output an video, it creates the video link at static if there does not already exist a video

