from flask import Flask, render_template
from flask_restful import Api
from blueprint import simple_page

from resources.route import initialize_routes
from database.db import initialize_db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "qrstock" # change this!

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.pgmzz.mongodb.net/Stockbeheer?retryWrites=true&w=majority' # Stockbeheer is naam van de db
}

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

app.register_blueprint(simple_page, url_prefix="/log")


if __name__== "__main__":
    app.run(host="192.168.56.1",debug =True) 




