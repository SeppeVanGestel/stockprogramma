from stockprogramma.database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from stockprogramma.database.models.product import Product

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    email = db.StringField(required=True)
    products = db.ListField(db.ReferenceField('Product', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)    



User.register_delete_rule(Product, 'added_by', db.CASCADE)        # user deleten is () ook deleten.