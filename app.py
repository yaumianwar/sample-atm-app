#!/usr/bin/python

import datetime
from flask import Flask, render_template, session, redirect
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
		email = request.get.form("email", None)
		password = request.get.form("password", None)
		confirm_password = request.get.form("confirm_password", None)
		bio = request.get.form("bio", None)
		avatar = request.get.form("avatar", None)

		errors = []
    	if full_name == "":
       		errors.append(dict(field="full_name",
                           message="Input Empty"))
    	if email == "":
        	errors.append(dict(field="email",
                           message="Input Empty"))
    	if password == "":
        	errors.append(dict(field="passwor",
                           message="Input Empty")) 
        if password != confirm_password:
       		errors.append(dict(field="confirm_password",
                           message="Password and Confirm Password Should be the same"))
    	if bio == "":
        	errors.append(dict(field="bio",
                           message="Input Empty"))
    	if avatar == "":
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