from flask import Blueprint, redirect, url_for, request, render_template

goods = Blueprint("goods", __name__)


@goods.route("/")
def index():
    username = request.args.get("username")
    if not username:
        return redirect(url_for("goods.login"))
    else:
        return render_template("index.html")


@goods.route("/login/")
def login():
    return render_template("goods.html")
