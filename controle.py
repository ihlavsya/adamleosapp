from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

simple_page = Blueprint("test", __name__, template_folder="templates")

@simple_page.route('/')
def index():
    return render_template('test.html')