from flask import Blueprint, request
from services.main_service import ProductService

# Blueprint for allow flak contorller modularity
main_controller = Blueprint('main_controller', __name__)

# Services import
service = ProductService()


# Source
@main_controller.route('/helloworld', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@main_controller.route('/products', methods=['GET'])
def get_products():
    products_sources = request.args.get('source')
    if products_sources is None:
        return service.get_products()
    if(products_sources  == "odoo"):
        return service.get_odoo_products()
    if(products_sources  == "prestashop"):
        return service.get_prestashop_products()
    return "Unknown source", 400

@main_controller.route('/products', methods=['POST'])
def post_product():
    products_target = request.args.get('target')
    body = request.get_json()

        # Vérifier si les champs requis existent dans les données
    if 'name' not in body or 'price' not in body or 'description' not in body:
        # Récupérer les valeurs des champs
        return "you mut pecify name, price and description in request body", 400
    if products_target is None:
        return "You must specify a target", 400
    if(products_target  == "odoo"):
        return service.create_odoo_products(body['name'], body['price'], body['description'])
    if(products_target  == "prestashop"):
        return service.create_prestashop_products(body['name'], body['price'], body['description'])
    return "Unknown source", 400

