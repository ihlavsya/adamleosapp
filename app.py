from flask import Flask, render_template
from views.old_posts import old_posts
from views.old_topics import old_topics
from views.media import media
from views.contacts import contacts
from views.posts import posts
from views.topics import topics


app = Flask(__name__)

# if app.config["ENV"] == "production":
#     app.config.from_object("config.ProductionConfig")
# else:
#     app.config.from_object("config.DevelopmentConfig")

app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(media, url_prefix='/media')
app.register_blueprint(contacts, url_prefix='/contacts')
app.register_blueprint(posts, url_prefix='/posts')
app.register_blueprint(old_posts, url_prefix='/posts')
app.register_blueprint(old_topics, url_prefix='/topics')
app.register_blueprint(topics, url_prefix='/topics')


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.shtml')

if __name__ == "__main__":
   app.run()