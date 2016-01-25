from flask import Blueprint, render_template


coreView = Blueprint('core', __name__, template_folder='../../templates')

@coreView.route("/")
def homepage():
    return render_template("home.html")
