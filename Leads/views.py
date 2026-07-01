from flask import Blueprint, render_template
from .models import Lead
from flask import jsonify


views = Blueprint("views", __name__)

@views.route("/thanks")
def thank_you():
    return render_template("thank_you.html")

