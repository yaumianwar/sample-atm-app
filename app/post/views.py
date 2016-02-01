import datetime
from flask import Blueprint, render_template
from app.core.db import database
from app.user.models import User
from models import Post, Comment, Like

post_views = Blueprint('post', __name__, template_folder='../../templates')

@post_views.route("/")
def listpost():
	list_post = Post.query.all()
	return render_template("posts.html",  **locals())

@post_views.route("/<slug>.html")
def onepost(slug):
	post = Post.query.filter_by(slug=slug)
	if not post:
		abort(404)
	return render_template("post.html",  **locals())

@post_views.route("/createpost/<int:id>",  methods = ["POST", "GET"])
def createpost(id):
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))

    if request.method == "POST":
        title= request.form.get("title", None)
        content = request.form.get("content", None)

        errors = []
        if title is None and title == "":
            errors.append(dict(field="title",
                                message="Input Empty"))
        if content is None and content == "":
            errors.append(dict(field="content",
                                message="Input Empty"))
        if len(errors) > 0:
            return render_template("create_post.html", **locals())


        post = Post(title, content)
        post.createdtime = datetime.datetime.now()
        database.session.add(post)
        database.session.commit()

        return redirect(url_for("post.listpost"))

    return render_template("create_post.html", **locals())
