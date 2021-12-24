from flask import Flask, render_template
from views.old_posts import old_posts

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


app.register_blueprint(old_posts, url_prefix='/posts')
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
   app.run()

# import os

# def generate_func_from_filename(filename):
#     func_name = filename.replace("-", "_").replace(".html", "")
#     template = f"""
# @old_posts.route('{filename}')
# def {func_name}():
#    return render_template('posts/{filename}')"""
#     return template


# def generate_funcs(output_filename, path):
#     funcs = []
#     output_file = open(output_filename, "a")
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             func = generate_func_from_filename(file)
#             output_file.writelines(func)
#             output_file.write("\n")
#     output_file.close()
#     return funcs


# if __name__ == "__main__":
#     generate_funcs("funcs.txt", "templates/posts")

