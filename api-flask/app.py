from flask import Flask, jsonify, request
from utils import Odoo

app = Flask(__name__)

@app.route('/')
def getActive():
    return jsonify({'message':'ok'})

@app.route('/products')
def getProduct():
    odoo = Odoo()
    response = odoo.get_product()
    return jsonify(response)

@app.route('/partner', methods=['POST'])
def getPartner():
    odoo = Odoo()
    response = odoo.get_partner(request.json['partnerEmail'])
    return jsonify({"id": response})

@app.route('/contact/add', methods=['POST'])
def createContact():
    odoo = Odoo()
    response = odoo.create_contact(request.json['name'], 
                                    request.json['phone'], 
                                    request.json['email'])
    return jsonify(response)

@app.route('/crm/add', methods=['POST'])
def createCRM():
    odoo = Odoo()
    response = odoo.create_crm(request.json['name'], 
                                    request.json['burger'], 
                                    request.json['partner_id'],
                                    request.json['phone'], 
                                    request.json['street'], 
                                    request.json['expected_revenue'])
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

