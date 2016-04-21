import datetime
from flask import Blueprint, render_template, redirect, session, request, abort, url_for
from slugify import slugify
from app.core.db import database
from app.user.models import User
from models import Transfer, Pemasukan, Penarikan
from app.user.views import user_views

post_views = Blueprint('post', __name__, template_folder='../../templates')


@post_views.route("/transfer",  methods = ["POST", "GET"])
def createtransfer():
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))

    if request.method == "POST":
        value= request.form.get("value", None)
        tujuan= request.form.get("tujuan", None)

        errors = []
        if value is None or value == "":
            errors.append(dict(field="value",
                                message="Input Empty"))
        if tujuan is None or tujuan == "":
            errors.append(dict(field="tujuan",
                                message="Input Empty"))
        if len(errors) > 0:
            return render_template("create_transfer.html", errors=errors), 400



        transfer = Transfer(value, tujuan, session.get("user_id", None))
        transfer.createdtime = datetime.datetime.now()
        user.saldo = int(user.saldo) - int(value)
        database.session.add(transfer)
        database.session.add(user)
        database.session.commit()

        return redirect(url_for("user.listtransaksi")), 201

    return render_template("create_transfer.html", **locals())

@post_views.route("/penarikan",  methods = ["POST", "GET"])
def createpenarikan():
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))

    if request.method == "POST":
        value= request.form.get("value", None)

        errors = []
        if value is None or value == "":
            errors.append(dict(field="value",
                                message="Input Empty"))

        if len(errors) > 0:
            return render_template("create_penarikan.html", errors=errors), 400

        penarikan = Penarikan(value, session.get("user_id", None))
        penarikan.createdtime = datetime.datetime.now()
        user.saldo = int(user.saldo) - int(value)
        database.session.add(penarikan)
        database.session.add(user)
        database.session.commit()

        return redirect(url_for("user.listtransaksi")), 201

    return render_template("create_penarikan.html", **locals())

@post_views.route("/pemasukan",  methods = ["POST", "GET"])
def createpemasukan():
    id = session.get("user_id", None)
    if id is None:
        return redirect(url_for("core.homepage"))
    user = User.query.get(id)
    if user is None:
        return redirect(url_for("core.homepage"))

    if request.method == "POST":
        value= request.form.get("value", None)

        errors = []
        if value is None or value == "":
            errors.append(dict(field="value",
                                message="Input Empty"))

        if len(errors) > 0:
            return render_template("create_pemasukan.html", errors=errors), 400

        pemasukan = Pemasukan(value, session.get("user_id", None))
        pemasukan.createdtime = datetime.datetime.now()
        user.saldo = int(user.saldo) + int(value)
        database.session.add(pemasukan)
        database.session.add(user)
        database.session.commit()

        return redirect(url_for("user.listtransaksi")), 201

    return render_template("create_pemasukan.html", **locals())
