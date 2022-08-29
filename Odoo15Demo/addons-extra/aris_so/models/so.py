from odoo import models, fields


class SalesOrderInherit(models.Model):
    _inherit = 'sale.order'

    no_kontrak = fields.Char(string='No Kontrak', )
    
