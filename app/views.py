from crypt import methods
import re
from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint('views', __name__)

@views.route('/intro', methods=["GET", "POST"])
def intro():
    if request.method == "POST":
        if request.form['iconButton'] == 'iconbtn':
            return redirect(url_for("/"))
    return render_template("intro.html")

@views.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form['docsButton'] == 'Docs':
            return redirect(url_for("/intro"))
    return render_template("home.html")