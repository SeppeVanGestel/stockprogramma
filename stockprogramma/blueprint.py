
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, static_folder="static",
                        template_folder='templates')

@simple_page.route('/home') #/log/home
@simple_page.route('/') # /log/ -> gaat naar blueprint
def home():
    try:
        return render_template('home.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/login')
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/signup')
def signup():
    try:
        return render_template('signup.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route('/add_product', methods=["POST","GET"])
def add():
    try:
        return render_template('add_product.html')
    except TemplateNotFound:
        abort(404)        