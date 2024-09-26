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

@bp.route("/projects/athlete_progan")
def athlete_progan():
    return render_template("pages/athlete_progan.html")

@bp.route("/projects/map_generator")
def map_generator():
    return render_template("pages/map_generator.html")

@bp.route("/projects/football_simulator")
def football_simulator():
    return render_template("pages/football_simulator.html")

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
