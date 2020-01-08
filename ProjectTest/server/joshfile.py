import moviepy.editor as mp

#creates the thisisknife video
def uploadvideo(video):
    clip = mp.VideoFileClip(video).subclip(0,10)
    txt_clip = mp.TextClip("thisisknife",fontsize=70,color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(10)
    video = mp.CompositeVideoClip([clip, txt_clip])
    video.write_videofile("static/surgeryoutput.mp4")
