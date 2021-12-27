from flask import Blueprint, render_template

old_topics = Blueprint("old-topics", __name__)

@old_topics.route('sleep.html')
def sleep():
   return render_template('topics/sleep.html')

@old_topics.route('index.html')
def index():
   return render_template('topics/index.html')

@old_topics.route('fasting.html')
def fasting():
   return render_template('topics/fasting.html')

@old_topics.route('microbiome.html')
def microbiome():
   return render_template('topics/microbiome.html')

@old_topics.route('temperature-stress.html')
def temperature_stress():
   return render_template('topics/temperature-stress.html')