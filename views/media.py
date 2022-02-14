from flask import Blueprint, render_template

media = Blueprint("media", __name__)

@media.route('/')
@media.route('index.html')
def index():
   return render_template('media/index.html')

@media.route('videos')
@media.route('videos.html')
def videos():
   return render_template('media/videos.html')

@media.route('extra')
@media.route('extra.html')
def extra():
   return render_template('media/extra.html')

@media.route('kusochki')
@media.route('kusochki.html')
def kusochki():
   return render_template('media/kusochki.html')