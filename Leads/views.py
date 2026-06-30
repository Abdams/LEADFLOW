from flask import Blueprint, render_template
from .models import Lead
from flask import jsonify


views = Blueprint("views", __name__)

