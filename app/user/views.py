import datetime
from flask import Blueprint, render_template, request, redirect, session, url_for
from app.core.db import database
from app.core.bcrypt import bcrypt
from models import User


user_views = Blueprint('user', __name__, template_folder='../../templates')



@user_views.route("/regist", methods=["POST", "GET"])
def regist():
    if request.method == "POST":
        full_name = request.form.get("full_name", None)
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        confirm_password = request.form.get("confirm_password", None)
        bio = request.form.get("bio", None)
        avatar = request.form.get("avatar", None)

        errors = []
        if full_name is None or full_name == "":
            errors.append(dict(field="full_name",
                                message="Input Empty"))
        if email is None or email == "":
            errors.append(dict(field="email",
                                message="Input Empty"))
        if password is None or password == "":
            errors.append(dict(field="password",
                                message="Input Empty"))
        if password != confirm_password:
            errors.append(dict(field="confirm_password",
                                message="Password and Confirm Password Should be the same"))
        if bio is None or bio == "":
            errors.append(dict(field="bio",
                                message="Input Empty"))
        if avatar is None or avatar == "":
            errors.append(dict(field="avatar",
                                message="Input Empty"))
        if len(errors) > 0:
            return render_template("register.html", **locals())

        password = bcrypt.generate_password_hash(password)
        user = User(full_name, email, password, bio, avatar)
        user.registered = datetime.datetime.now()
        database.session.add(user)
        database.session.commit()

        session["user_id"] = user.id
        return redirect(url_for("core.homepage"))

    return render_template("register.html", **locals())

@user_views.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        errors = []
        if email != "" or password != "":
            user = User.query.filter_by(email=email).first()
            if user is not None:
                #verify user password
                if bcrypt.check_password_hash(user.password, password):
                    # update user.last_login to now
                    user.last_login = datetime.datetime.now()
                    database.session.add(user)
                    database.session.commit()
                    # save user id
                    session["user_id"] = user.id
                    return redirect(url_for("core.homepage"))

                else:
                    errors.append(dict(field="password_check",
                                        message="Your password is wrong"))
                    return render_template("login.html", **locals())

            else:
                errors.append(dict(field="email_check",
                                    message="Your email doesn't registered"))
                return render_template("login.html", **locals())

        else:
            errors.append(dict(field="password",
                                message="Input Empty"))
            errors.append(dict(field="email",
                                message="Input Empty"))
            return render_template("login.html", **locals())

    return render_template("login.html", **locals())

@user_views.route("/userlist")
def userlist():
    user = User.query.all()
    return render_template("list_user.html", **locals())

@user_views.route("/profile/<int:id>")
def profileuser(id):
    user = User.query.get(id)
    if not user:
        abort(404)
    return render_template("user_profile.html",  **locals())

@user_views.route("/profile")
def user():
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))
    return render_template("profile.html",  **locals())
