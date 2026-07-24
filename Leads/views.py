from flask import Blueprint, render_template
from .models import Lead
from flask import jsonify


views = Blueprint("views", __name__)


@views.route("/UroNature", methods=["GET", "POST"])
def Uronature():
    return render_template("Uronature.html")

@views.route("/Cardiotens", methods=["GET", "POST"])
def Cardiotens():
    return render_template("Cardiotens.html")

@views.route("/Tensinorm", methods=["GET", "POST"])
def Tensinorm():
    return render_template("Tensinorm.html")

@views.route("/Cartiofin", methods=["GET", "POST"])
def Cartiofin():
    return render_template("Cartiofin.html")

@views.route("/Movita", methods=["GET", "POST"])
def Movita():
    return render_template("Movita.html")

@views.route("/Glowycare", methods=["GET", "POST"])
def Glowy():
    return render_template("Glowy.html")

@views.route("/Carditone", methods=["GET", "POST"])
def Carditone():
    return render_template("Carditone.html")

@views.route("/Veniselle", methods=["GET", "POST"])
def Veniselle():
    return render_template("Veniselle.html")

@views.route("/Artralon", methods=["GET", "POST"])
def Artralon():
    return render_template("Artralon.html")

@views.route("/thanks")
def thank_you():
    return render_template("thank_you.html")

