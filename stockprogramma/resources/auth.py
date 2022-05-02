from flask import Flask, jsonify, request
from stockprogramma.database.models.users import User
from flask_restful import Resource
from flask import Response, request
from flask_jwt_extended import create_access_token
import datetime

from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from stockprogramma.resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
InternalServerError



class SignupUi(Resource): #signup erft van resource(een class uit flas restfull...) ipv de body komt de input nu vanuit de form
 def post(self):

        try:
            body = request.get_json()
            user = User(**body).get()
            name = request.get_json("name") # name = vanwaar komt "name"??? index -> <input type="text" class="form-control" name="name">
            pwd = request.get_json("password") #
            username = request.get_json("username") #
            user = User(name=name, password=pwd, username=username) #
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 200 # geeft een hashed user_id terug
            
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginUi(Resource): # het bearer token moet hier ergens meegegeven worden om in de url te gaan...
    def post(self):
        
        try:
            user = user.get_json(force=True) 
            authorized = user.check_password(request.get_json("password")) # pwd = request.form.get("password")
            if not authorized:
                return {'error': 'Email or password invalid'}, 401
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200 # geeft een bearer token terug als response op /api/auth/loginui
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError              