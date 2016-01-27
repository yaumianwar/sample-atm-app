from flask import Blueprint, render_template
from app.core.db import database
from models import Post, Comment, Like

post_views = Blueprint('post', __name__, template_folder='../../templates')

@post_views.route("/")
def listpost():
	list_post = Post.query.all()
	return render_template("list_post.html",  **locals())

@post_views.route("/<slug>.html")
def post(slug):
	post = Post.query.filter_by(slug=slug)
	if not post:
		abort(404)
	return render_template("post.html",  **locals())
