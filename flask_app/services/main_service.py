from clients.odoo_client import OdooClient
from clients.prestashop_client import PrestaShopClient

class ProductService:
    def __init__(self):
        self.odooClient = OdooClient()
        self.prestashopClient = PrestaShopClient()
        
    def get_prestashop_products(self):
        return ['presta_User1', 'presta_User2', 'presta_User3']
    
    def get_odoo_products(self):
        return self.odooClient.get_products()
    
    def create_prestashop_products(self, name, price, description):
        return self.prestashopClient.create_products(name, price, description)
    
    def create_odoo_products(self, name, price, description):    
        return self.odooClient.create_products(name, price, description)
        
    def get_products(self):    
        return self.get_odoo_products() + self.get_prestashop_products()

