# -*- coding: utf-8 -*-

from odoo import fields, models, api
from random import randint


class ProductTemplate(models.Model):
    _inherit = "product.template"
   
    city = fields.Char('City')
    zone = fields.Char('Zone')
    location = fields.Char('Location')
    width = fields.Char('Width')
    height = fields.Char('Height')
    total_area = fields.Char('Total Area')
    formats = fields.Many2many('format.type', string="Formats")
    space_type = fields.Many2one('space.type', string="Type of Support")
    daily_impacts = fields.Char('Daily Impacts')
    cost_per_impact = fields.Float('Cost Per Impact')
    has_lighting = fields.Boolean('Has Lighting')
    lighting_type = fields.Many2one('lighting.type', string="Type of Lighting")
    printing_substrate = fields.Many2one('printing.substrate', string="Printing Substrate")
    image_1 = fields.Image("Image 1")
    image_2 = fields.Image("Image 2")
    image_map = fields.Image("Map Image")
    printing_cost = fields.Float('Printing Cost')
    installation_cost = fields.Float('Installation Cost')


class SpaceType(models.Model):
    _name = "space.type"
    _description = "Space Type"

    name = fields.Char('Name')


class LightingType(models.Model):
    _name = "lighting.type"
    _description = "Lighting Type"

    name = fields.Char('Name')


class PrintingSubstrate(models.Model):
    _name = "printing.substrate"
    _description = "Printing Substrate"

    name = fields.Char('Name')


class FormatType(models.Model):
    _name = "format.type"
    _description = "Format Type"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)
