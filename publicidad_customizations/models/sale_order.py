# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    width = fields.Float('Width')
    product_uom_name = fields.Char(related="product_uom.name")
    height = fields.Float('Height')
    total_in_m2 = fields.Float('Total in m²', compute="_compute_total_in_m2")
    design_image = fields.Image('Design Image')

    @api.depends('width', 'height', 'product_uom_qty')
    def _compute_total_in_m2(self):
        for line in self:
            line.total_in_m2 = line.width * line.height * line.product_uom_qty

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'total_in_m2')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        return super(SaleOrderLine, self)._compute_amount()

    def _convert_to_tax_base_line_dict(self):
        """ Convert the current record to a dictionary in order to use the generic taxes computation method
        defined on account.tax.

        :return: A python dictionary.
        """
        self.ensure_one()

        quantity = self.product_uom_qty
        if self.product_uom.name == 'm²' and self.total_in_m2:
            quantity = self.total_in_m2

        return self.env['account.tax']._convert_to_tax_base_line_dict(
            self,
            partner=self.order_id.partner_id,
            currency=self.order_id.currency_id,
            product=self.product_id,
            taxes=self.tax_id,
            price_unit=self.price_unit,
            quantity=quantity,
            discount=self.discount,
            price_subtotal=self.price_subtotal,
        )
