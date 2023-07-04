# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    width = fields.Float('Width')
    product_uom_name = fields.Char(related="product_uom.name")
    height = fields.Float('Height')
    display_image = fields.Boolean('Display Image')

    @api.depends('display_type', 'product_id', 'product_packaging_qty', 'width', 'height')
    def _compute_product_uom_qty(self):
        res = super(SaleOrderLine, self)._compute_product_uom_qty()
        for line in self:
            if line.product_uom.name == 'm²':
                line.product_uom_qty = (line.width * line.height) or 1.0
        return res

