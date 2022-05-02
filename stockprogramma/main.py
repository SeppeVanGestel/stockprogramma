from flask import Flask, render_template
from flask_restful import Api
import os, sys





from resources.route import initialize_routes
from database.db import initialize_db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

if os.environ.get("JWT_SECRET_KEY") is None:
    load_dotenv()

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY') # change this!

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('uri') # Stockbeheer is naam van de db
}

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)




if __name__== "__main__":
    app.run(host="192.168.56.1",debug =True) 




