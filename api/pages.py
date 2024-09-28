from flask import Blueprint, render_template, redirect, send_file, request
from api.projects.athlete_progan.eval import gen_images
from torchvision.utils import save_image
import os
import io
from PIL import Image
import numpy as np

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

@bp.route('/generate', methods=['POST'])
def generate():
    team = request.form.get('team')
    skin_tone = request.form.get('skin-tone')
    build = request.form.get('build')

    # Generate image using your model
    images = gen_images(team, skin_tone, build)
    img1 = images[0]
    img1 = img1.detach().numpy()
    img1 = np.transpose(img1, (1, 2, 0))
    img1 = ((img1 * 0.5 + 0.5) * 255).astype(np.uint8)
    pil_image = Image.fromarray(img1)

    # Save the image to an in-memory buffer
    img_io = io.BytesIO()
    pil_image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
