from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Response, request
from flask_restful import Resource
from flask import jsonify
from stockprogramma.database.models.product import Product
from stockprogramma.database.models.users import User




from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from stockprogramma.resources.errors import SchemaValidationError, ProductAlreadyExistsError, \
InternalServerError, UpdatingProductError, DeletingProductError, ProductNotExistsError
from stockprogramma.resources.errors import ProductAlreadyExistsError

class ProductsApi(Resource):
    @jwt_required() # jwt maakt token voor de cliënt
    def get(self):
        products = Product.objects().to_json() # zet models.product om in een json object (een dict)
        return Response(products, mimetype="application/json", status=200) # returned het json object en de melding ...
    
    @jwt_required() # hoe geef ik hier het bearer token mee??? -> ik denk ergens anders inloggen en bearer ergens invullen...
    def post(self):
        
        try:
            user_id = get_jwt_identity()
            print(user_id)
            body = request.get_json()
            print(body)
            user = User.objects.get(id=user_id)
            product = Product(**body, added_by=user.to_dbref())
            product.save()
            user.update(push__products=product)
            user.save() # user = User(**body).save() # sla data van json op in de db
            id = product.id
            return {'id': str(id)}, 200

        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProductAlreadyExistsError
        except Exception as e:
            raise InternalServerError
 
class ProductApi(Resource): 
    @jwt_required()
    def put(self, id):
        
        try:
            user_id = get_jwt_identity()
            product = Product.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            product.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingProductError
        except Exception:
            raise InternalServerError