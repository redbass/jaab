from flask import render_template


def jaab():
    return render_template("app.jinja2")


def get_template(name):
    return render_template(name + ".jinja2")
