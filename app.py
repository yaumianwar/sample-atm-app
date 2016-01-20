#!/usr/bin/python

import datetime
from flask import Flask, render_template, session, redirect, request
from db import database
from models import User


app = Flask(__name__)
app.config.from_object('config')
database.init_app(app)

@app.route("/")
def homepage():
  user = User.query.filter_by(id=1).first()
  return render_template("home.html",  **locals())

@app.route("/regist", methods=["POST", "GET"])
def regist():
	if request.method == "POST":
		full_name = request.form.get("full_name", None)
		email = request.form.get("email", None)
		password = request.form.get("password", None)
		confirm_password = request.form.get("confirm_password", None)
		bio = request.form.get("bio", None)
		avatar = request.form.get("avatar", None)

		errors = []
    if full_name is None and full_name == "":
      errors.append(dict(field="full_name",
                        message="Input Empty"))
    if email is None and email == "":
      errors.append(dict(field="email",
                        message="Input Empty"))
    if password is None and password == "":
      errors.append(dict(field="passwor",
                        message="Input Empty")) 
    if password != confirm_password:
      errors.append(dict(field="confirm_password",
                        message="Password and Confirm Password Should be the same"))
    if bio is None and bio == "":
      errors.append(dict(field="bio",
                        message="Input Empty"))
    if avatar is None avatar == "":
      errors.append(dict(field="avatar",
                        message="Input Empty"))   
    if len(errors) > 0:
      return render_template("register.html", **locals())

    user = User(full_name, email, password, bio, avatar)
    db.session.add(user)
    db.session.commit()

    session["user_id"] = user.id
    return redirect("home.html", **locals())

  # return render_template("register.html", **locals())

@app.route("/login", methods = "GET")
def login():
  email = request.form.get("email", None)
  password = request.form.get("password", None)
  if email != "" or password != "":
    user = User.query.filter_by(email=email).first()
    if user is not None:
      #verify user password
      if user.password == password:
        # update user.last_login to now
        user.last_login = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        # save user id
        session["user_id"] = user.id
        return redirect("/")

      else:
        return render_template("login.html", **locals())  

    else:     
      return render_template("login.html", **locals())

  else:
    return render_template("login.html", **locals())  


if __name__=="__main__":
  app.run(debug=True)