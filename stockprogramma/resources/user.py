from stockprogramma.database.models.users import User
from flask import Response, request
from flask_restful import Resource


class UsersApi(Resource): # resource maakt de url routes, put, get, post ,... per resource kan je crud doen
    def get(self): # laat data zien
        users = User.objects().to_json() # User. objects is een actie van mongoengine, ga op db naar user en zet naar json
        return Response(users, mimetype="application/json", status=200) # geef de gevraagde json data weer

    def post(self):
        body = request.get_json() # data van postman of form
        print(body)
        user = User(**body).save() # sla data van json op in de db
        id = user.id
        return {'id': str(id)}, 200 # geef nieuwe id mee ter bevestiging
   