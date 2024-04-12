import xmlrpc.client
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class OdooClient:
    def __init__(self):
        self.url = os.getenv('ODOO_URL')
        self.db = os.getenv('ODOO_DB_NAME')
        self.username = os.getenv('ODOO_ADMIN_USERNAME')
        self.password = os.getenv('ODOO_ADMIN_PASSWORD')

        # Connexion à l'instance Odoo
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        self.connection = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def get_client(self):
        # Authentification et récupération de l'UID
        self.connection
    
    def get_products(self):
        # Création d'une nouvelle connexion pour l'API
        models = self.connection

        # Recherche des produits et récupération de leurs informations
        product_ids = models.execute_kw(self.db, self.uid, self.password,
            'product.product', 'search', [[]])  

        products = models.execute_kw(self.db, self.uid, self.password,
            'product.product', 'read', [product_ids], {'fields': ['name', 'list_price', 'description']})

        # Affichage des informations des produits
        for product in products:
            print("Nom du produit:", product['name'])
            print("Prix du produit:", product['list_price'])
            print("Description du produit:", product['description'])
            print("-----------------------------------")
        
        return products
    
    def create_products(self, name, price, description):
        print("try create product !")
        # Création d'une nouvelle connexion pour l'API
        models = self.connection

        # Création d'un nouveau produit
        product_id = models.execute_kw(self.db, self.uid, self.password,
            'product.product', 'create', [{
                'name': name,
                'list_price': price,
                'description': description
            }])

        # Vérification si le produit a été créé avec succès
        if product_id:
            print("Le produit a été créé avec succès !")
            print(product_id)
            return "", 201
        else:
            print("Erreur lors de la création du produit.")
            return None
    

 