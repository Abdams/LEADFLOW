from flask import Blueprint, render_template, redirect, url_for, request, Response, session
from .extensions import db
from config import ADMIN_EMAIL, ADMIN_PASSWORD, Webhook_url
from .models import Lead, datetime
from functools import wraps
import requests


auth = Blueprint("auth", __name__)

@auth.route("/Virex", methods=["GET"])
def Virex():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("virex.html")


@auth.route("/Avital", methods=["GET"])
def Avital():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Avital.html")

@auth.route("/Fisio-forte", methods=["GET"])
def Fisio():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Fisio.html")

@auth.route("/Gluconat", methods=["GET"])
def Gluconat():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Gluconat.html")

@auth.route("/Artiflex", methods=["GET"])
def Artiflex():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Artiflex.html")

@auth.route("/Bururan", methods=["GET"])
def Bururan():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Bururan.html")

@auth.route("/Calmano", methods=["GET"])
def Calmano():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Calmano.html")

@auth.route("/Cortitron", methods=["GET"])
def Cortitron():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Cortitron.html")

@auth.route("/Deeplex", methods=["GET"])
def Deeplex():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Deeplex.html")

@auth.route("/Kettochi", methods=["GET"])
def Kettochi():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("kettochi.html")

@auth.route("/Otoryx", methods=["GET"])
def Otoryx():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Otoryx.html")

@auth.route("/Urodoc", methods=["GET"])
def Urodoc():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Urodoc.html")

@auth.route("/Urozex", methods=["GET"])
def Urozex():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Urozex.html")

@auth.route("/Vizilax", methods=["GET"])
def Vizilax():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        country = request.form.get("country")
        product = request.form.get("product")

        new_lead = Lead(
           full_name=full_name,
            phone=phone,
           country=country,
           product=product,
           product_type=product_type
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for("views.thank_you"))
    
    return render_template("Vizilax.html")

@auth.route("/Submit", methods=["GET", "POST"])
def Submit():
    full_name = request.form.get("full_name")
    phone = request.form.get("phone")
    country = request.form.get("country")
    product = request.form.get("product")

    lead = Lead(
        full_name=full_name,
        phone=phone,
        country=country,
        product=product
    )

    db.session.add(lead)
    db.session.commit()

    response = requests.post(
        Webhook_url,
        json={
            "full_name": full_name,
           "phone": phone,
           "country": country,
           "product": product
        }
    )
    print("Sent to n8n")

    return render_template("thank_you.html")

    
def dashboard_login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("auth.admin_login"))
        return view(*args, **kwargs)

    return wrapped_view

@auth.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if email.lower() == ADMIN_EMAIL.lower() and password == ADMIN_PASSWORD:
            session.clear()
            session["admin_logged_in"] = True
            session["admin_email"] = email
            return redirect(url_for("auth.admin_leads"))

        error = "Invalid email or password."

    return render_template("admin_login.html", error=error)


@auth.route("/admin/leads")
@dashboard_login_required
def admin_leads():
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    total_leads = len(leads)
    new_leads = sum(1 for lead in leads if lead.status == "New")
    products = len({lead.product for lead in leads if lead.product})

    return render_template(
        "admin_leads.html",
        leads=leads,
        total_leads=total_leads,
        new_leads=new_leads,
        products=products
    )


@auth.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("auth.admin_login"))

@auth.route("/admin")
def admin_home():
    return redirect(url_for("auth.admin_leads"))

@auth.route("/check-db")
def check_db():
    leads = Lead.query.all()

    return "<br>".join(
        f"{lead.full_name} - {lead.phone} - {lead.country} - {lead.product}"
        for lead in leads
    )