from flask import Blueprint, render_template

contacts = Blueprint("contacts", __name__)

@contacts.route('/')
@contacts.route('index.html')
def index():
   return render_template('contacts/index.html')