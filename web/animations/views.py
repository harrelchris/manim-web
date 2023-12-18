from flask import render_template, request
from . import forms
import uuid
import web.settings
from scenes.circle import CreateCircle, CreateCircleParams


def index():
    return render_template("animations/index.html")


def circle():
    form = forms.CreateCircleForm()
    file_path = "media/default/CreateCircle.mp4"
    if request.method == "POST":
        if form.validate_on_submit():
            params = CreateCircleParams(
                radius=request.form["radius"],
            )
            c = CreateCircle(params=params)
            file_name = f"{uuid.uuid4().hex}.mp4"
            c.renderer.file_writer.movie_file_path = web.settings.DYNAMIC_VIDEO_DIR / file_name
            c.render()
            file_path = f"media/dynamic/{file_name}"
    return render_template("animations/circle.html", file_path=file_path, form=form)
