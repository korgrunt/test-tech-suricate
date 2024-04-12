# services
import xmlrpc.client
from dotenv import load_dotenv
import os

# Informations de connexion à votre instance Odoo
url = os.getenv('ODOO_URL')
db = os.getenv('ODOO_DB_NAME')
username = os.getenv('ODOO_ADMIN_USERNAME')
password = os.getenv('ODOO_ADMIN_PASSWORD')

# Connexion à l'instance Odoo
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})


class ProductService:
    def get_prestashop_products(self):
        return ['presta_User1', 'presta_User2', 'presta_User3']
    
    def get_odoo_products(self):
        # Création d'une nouvelle connexion pour l'API
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

        # Recherche des produits et récupération de leurs informations
        product_ids = models.execute_kw(db, uid, password,
            'product.product', 'search', [[]])  # Récupérer les 10 premiers produits par exemple

        products = models.execute_kw(db, uid, password,
            'product.product', 'read', [product_ids], {'fields': ['name', 'list_price', 'description']})

        # Affichage des informations des produits
        for product in products:
            print("Nom du produit:", product['name'])
            print("Prix du produit:", product['list_price'])
            print("Description du produit:", product['description'])
            print("-----------------------------------")
        
        return products
    
    def create_prestashop_products(self):
        return ['presta_User1', 'presta_User2', 'presta_User3']
    
    def create_odoo_products(self):    
        return ['odoo_User1', 'odoo_User2', 'odoo_User3']
    
        
    def get_products(self):    
        return self.get_odoo_products() + self.get_prestashop_products()

