import datetime
from flask import Blueprint, jsonify, Response, render_template, request, redirect, session, url_for
from app.core.db import database
from app.core.bcrypt import bcrypt
from models import User
from app.transaksi.models import Transfer, Pemasukan, Penarikan


user_views = Blueprint('user', __name__, template_folder='../../templates')



@user_views.route("/regist", methods=["POST", "GET"])
def regist():
    if request.method == "POST":
        norek = request.form.get("norek", None)
        saldo = request.form.get("saldo", None)
        avatar = request.form.get("avatar", None)
        password = request.form.get("password", None)
        confirm_password = request.form.get("confirm_password", None)

        errors = []
        if norek is None or norek == "":
            errors.append(dict(field="norek",
                                message="Input Empty"))
        if avatar is None or avatar == "":
            errors.append(dict(field="avatar",
                                message="Input Empty"))
        if saldo is None or saldo == "":
            errors.append(dict(field="saldo",
                                message="Input Empty"))
        if password is None or password == "":
            errors.append(dict(field="password",
                                message="Input Empty"))
        if password != confirm_password:
            errors.append(dict(field="confirm_password",
                                message="Password and Confirm Password Should be the same"))
        if len(errors) > 0:
            return render_template("register.html", **locals())

        password = bcrypt.generate_password_hash(password)
        user = User(norek, password, saldo, avatar)
        user.registered = datetime.datetime.now()
        database.session.add(user)
        database.session.commit()

        session["user_id"] = user.id
        return redirect(url_for("core.homepage"))

    return render_template("register.html", **locals())

@user_views.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        norek = request.form.get("norek", None)
        password = request.form.get("password", None)
        errors = []
        if norek != "" or password != "":
            user = User.query.filter_by(norek=norek).first()
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
                    resp = jsonify(dict(errors=errors))
                    resp.status_code = 400
                    return resp

            else:
                errors.append(dict(field="norek_check",
                                    message="Your rekening number doesn't registered"))
                return render_template("login.html", **locals())

        else:
            errors.append(dict(field="password",
                                message="Input Empty"))
            errors.append(dict(field="norek",
                                message="Input Empty"))
            return render_template("login.html", **locals())

    return render_template("login.html", **locals())

@user_views.route("/profile")
def user():
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))
    return render_template("profile.html",  **locals())

@user_views.route("/transaksi")
def listtransaksi():
    user_id = session.get("user_id", None)
    if user_id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(user_id)
    if user is None:
        return redirect(url_for("core.homepage"))

    transfer = Transfer.query.filter_by(id_user=user_id)
    penarikan = Penarikan.query.filter_by(id_user=user_id)
    pemasukan = Pemasukan.query.filter_by(id_user=user_id)
    return render_template("transaksi.html",  **locals())

@user_views.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for("core.homepage"))
