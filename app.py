from flask import Flask, render_template
from views.old_posts import old_posts
from views.old_topics import old_topics

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


app.register_blueprint(old_posts, url_prefix='/posts')
app.register_blueprint(old_topics, url_prefix='/topics')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/media')
@app.route('/media/index.html')
def media_index():
    return render_template('media/index.html')


@app.route('/contacts')
@app.route('/contacts/index.html')
def contacts_index():
    return render_template('contacts/index.html')

if __name__ == "__main__":
   app.run()