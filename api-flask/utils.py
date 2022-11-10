import requests

class Odoo():
    def __init__(self):
        self.url = "http://web-odoo:8069/jsonrpc"

    def get_product(self):
        json_sent = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "service": "object", 
                            "method": "execute", 
                            "args": ["odooBurger", 2, "admin", "product.product", "search", [], []]
                        }
                    }
        response = requests.post(self.url, json = json_sent)
        json = []
        for product in response.json()['result']:
            new_product={}
            new_product['id']=product['id']
            new_product['name']=product['name']
            new_product['lst_price']=product['lst_price']
            json.append(new_product)

        return json

    def get_partner(self, partnerEmail):
        json_sent = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "service": "object", 
                            "method": "execute", 
                            "args": ["odooBurger", 2, "admin", "res.partner", "search_read", [["email", "=", partnerEmail]], []]
                        }
                    }
        response = requests.post(self.url, json = json_sent)
        return response.json()['result'][0]['id']

    def create_contact(self, name, phone, email):
        json_sent = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "service": "object", 
                            "method": "execute", 
                            "args": ["odooBurger", 2, "admin", "res.partner", "create", 
                            {
                                "name": name, 
                                "phone": phone, 
                                "email": email
                            }]
                        }
                    }
        response = requests.post(self.url, json = json_sent)
        return response
        

    def create_crm(self, name, burger, partner_id, phone, street, expected_revenue):
        json_sent = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "service": "object", 
                            "method": "execute", 
                            "args": ["odooBurger", 2, "admin", "crm.lead", "create", 
                                {
                                    "name": name, 
                                    "burger": burger, 
                                    "partner_id": int(partner_id),
                                    "phone": phone,
                                    "street": street,
                                    "expected_revenue": int(expected_revenue)
                                }]
                        }
                    }
        response = requests.post(self.url, json = json_sent)
        return response
