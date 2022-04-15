from stockprogramma.resources.product import ProductsApi
from stockprogramma.resources.user import UsersApi
from stockprogramma.resources.user import UsersApi
from stockprogramma.resources.auth import SignupUi, LoginUi



def initialize_routes(api): 
    api.add_resource(SignupUi, '/api/auth/signupui') 
    api.add_resource(LoginUi, '/api/auth/loginui') # dit is de response, de request is log/login uit de blueprint, staat ook in het form
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(ProductsApi, '/api/products')