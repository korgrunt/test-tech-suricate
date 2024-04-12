# services
class ProductService:
    def get_prestashop_products(self):
        return ['presta_User1', 'presta_User2', 'presta_User3']
    
    def get_odoo_products(self):    
        return ['odoo_User1', 'odoo_User2', 'odoo_User3']
    
    def create_prestashop_products(self):
        return ['presta_User1', 'presta_User2', 'presta_User3']
    
    def create_odoo_products(self):    
        return ['odoo_User1', 'odoo_User2', 'odoo_User3']
    
        
    def get_products(self):    
        return self.get_odoo_products() + self.get_prestashop_products()

