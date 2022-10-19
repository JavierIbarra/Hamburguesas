import xmlrpc.client
from django.conf import settings

class Odoo():
    def __init__(self) -> None:
        self.DATA = settings.DB_ODOO
        self.USER = settings.USER_ODOO
        self.PASS = settings.TOKEN_ODOO
        self.PORT = "8069"
        self.URL = settings.URL_ODOO
        self.URL_COMMON = "{}:{}/xmlrpc/2/common".format(self.URL, self.PORT)
        self.URL_OBJECT = "{}:{}/xmlrpc/2/object".format(self.URL, self.PORT)

    def authenticateOdoo(self):
        self.ODOO_COMMON = xmlrpc.client.ServerProxy(self.URL_COMMON)
        self.ODOO_OBJECT = xmlrpc.client.ServerProxy(self.URL_OBJECT)
        self.UID = self.ODOO_COMMON.authenticate(self.DATA, self.USER, self.PASS, {})

    def partnerAdd(self, partnerRow):
        partner_id = self.ODOO_OBJECT.execute_kw(
            self.DATA,
            self.UID,
            self.PASS,
            'res.partner',
            'create',
            partnerRow)

        return partner_id

    def CrmAdd(self, productRow):
        crm_id = self.ODOO_OBJECT.execute_kw(
            self.DATA,
            self.UID,
            self.PASS,
            'crm.lead',
            'write',
            productRow)

        return crm_id
