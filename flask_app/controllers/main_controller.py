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
