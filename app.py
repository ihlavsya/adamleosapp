import os
import sys
from flask import Flask, render_template
from controle import simple_page

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(simple_page, url_prefix='/pages')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
   app.run()