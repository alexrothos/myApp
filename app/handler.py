from pytube import YouTube
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class UrlForm(FlaskForm):
    url = StringField('URL : ')
    submit = SubmitField('Download')
    

def down(url,remote):
    yt = YouTube(url)
    print("Title : ", yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download('./YTDownloader')
    
