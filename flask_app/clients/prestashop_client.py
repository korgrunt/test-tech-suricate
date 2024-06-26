import os
import requests
import json
import xml.etree.ElementTree as ET

headers = {
    "Content-Type": "application/xml",
    "Accept": "application/xml",
    "Authorization": f"Basic {os.getenv('PRESTASHOP_API_KEY_BASE_64')}"
}

class PrestaShopClient:
    def __init__(self):
        self.prestashop_url = os.getenv('PRESTASHOP_URL')

    def get_products(self):
        response = requests.request("GET", self.prestashop_url, headers=headers)
        print(response)
        tree = ET.fromstring(response.text)

        # Récupère tous les éléments <product>
        products = tree.findall('.//product')

        data = []
        # Boucle à travers chaque produit
        for product in products:
            # Récupère l'attribut 'xlink:href' pour obtenir l'URL de l'API du produit
            print(product.attrib['id'])
            response = requests.request("GET", f"{self.prestashop_url}/{product.attrib['id']}", headers=headers)
            print(response.text)
            prodct_tree = ET.fromstring(response.text)

            product_as_xml = prodct_tree.findall('.//product')[0]
            print("====================")
            print(product_as_xml.find('price').text.strip())
            print(product_as_xml.find('price').text.strip())
            item = {
                "description": "",
                "id": product.attrib['id'],
                "list_price": product_as_xml.find('price').text.strip(),
                "name": product_as_xml.find('.//name/language').text.strip()
            }
            data.append(item)
            
        json_data = json.dumps(data, indent=4)
        return json_data
           
        
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
