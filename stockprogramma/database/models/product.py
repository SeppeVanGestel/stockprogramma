#~stockprogramma/database/models.py
from stockprogramma.database.db import db

class Product(db.Document):
    
    id = db.ListField(db.StringField(), required=True)
    name = db.StringField(required=True, unique=True)
    supply = db.IntField(required=True)
    min_stock = db.IntField(required=True)
    purchaseprice = db.DecimalField(precision=2, required=True)
    supplier = db.StringField(required=True, unique=True)

    added_by = db.ReferenceField('User')

    