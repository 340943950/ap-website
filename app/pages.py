from flask import Blueprint, render_template, redirect

bp = Blueprint("pages", __name__)

@bp.route("/")
def start():
    return redirect("/home")

@bp.route("/home")
def home():
    return render_template("pages/home.html")

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")

@bp.route("/experience")
def experience():
    return render_template("pages/experience.html")

@bp.route("/skills")
def skills():
    return render_template("pages/skills.html")

@bp.route("/resume")
def resume():
    return render_template("pages/resume.html")

@bp.route("/contact")
def contact():
    return render_template("pages/contact.html")
