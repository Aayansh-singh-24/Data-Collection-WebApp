from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from . import db
from .models import Submission


main_bp = Blueprint("main", __name__)


@main_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("All fields are required.", "danger")
            return render_template("index.html")

        submission = Submission(name=name, email=email, message=message)
        db.session.add(submission)
        db.session.commit()

        flash("Your data has been saved successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("index.html")


def register_blueprints(app):
    app.register_blueprint(main_bp)

