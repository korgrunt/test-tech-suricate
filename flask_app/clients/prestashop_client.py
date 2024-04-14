import os
import requests

headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml",
    "Authorization": f"Basic {os.getenv('PRESTASHOP_API_KEY_BASE_64')}"
}

class PrestaShopClient:
    def __init__(self):
        self.prestashop_url = os.getenv('PRESTASHOP_URL')
         
    def create_products(self, name, price, description):
        product_xml = f'''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
        <prestashop xmlns:xlink=\"http://www.w3.org/1999/xlink\">
        <product>
        <name>
        <language id=\"1\">
        <![CDATA[{name}]]>
        </language>
        </name>
        <price><![CDATA[{price}]]></price>
        </product>
        </prestashop>'''
        print(product_xml)
        print(self.prestashop_url)
        print(headers)
        print(os.getenv('PRESTASHOP_API_KEY'))
        # Corps XML à envoyer
        response = requests.request("POST", self.prestashop_url, data=product_xml, headers=headers)
        # Vérification de la réponse
        if response.status_code == 201:
            print("Produit ajouté avec succès !")
            return "", 201
        else:
            print(f"Échec de l'ajout du produit : {response.status_code}")
            return None
