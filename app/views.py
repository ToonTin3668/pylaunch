from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    pass
    #return render_template("index.html")

@views.route('/intro')
def intro():
    pass
    #return render_template("index.html")
