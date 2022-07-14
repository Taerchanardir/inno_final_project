from flask import Flask, render_template, Blueprint, redirect, url_for
my_view = Blueprint('my_view', __name__)

@my_view.route('/')
def index():
  return render_template("index.html")

@my_view.route('/villagers')
def villagers():
  return render_template("villagers.html")

@my_view.route('/endermen')
def endermen():
  return render_template("endermen.html")

@my_view.route('/chickens')
def chickens():
  return render_template("chickens.html")

@my_view.route('/cats')
def cats():
  return render_template("cats.html")

@my_view.route('/zombies')
def zombies():
  return render_template("zombies.html")

@my_view.route('/golems')
def golems():
  return render_template("golems.html")

@my_view.route('/js')
@my_view.route('/javascript')
@my_view.route('/home')
def general_redirects():
  return redirect(url_for("my_view.index"))

# @my_view.route('/admin')
# def admin_page():
#   return render_template("admin.html")



