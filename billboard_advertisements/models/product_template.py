# -*- coding: utf-8 -*-

import googlemaps

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
    space_type = fields.Many2one('space.type', string="Type of Space")
    daily_impacts = fields.Char('Daily Impacts')
    cost_per_impact = fields.Char('Cost Per Impact')
    has_lighting = fields.Boolean('Has Lighting')
    lighting_type = fields.Many2one('lighting.type', string="Type of Lighting")
    image_1 = fields.Image("Image 1")
    image_2 = fields.Image("Image 2")

    @api.model
    def get_google_map_url(self):
        if self:
            gmaps = googlemaps.Client(key='')
            address = "{}, {}, {}, {}".format(
                self.street or '', self.city or '', self.state_id.name or '', self.country_id.name or ''
            )
            location = gmaps.geocode(address)
            if location:
                lat = location[0]['geometry']['location']['lat']
                lng = location[0]['geometry']['location']['lng']
                return "https://www.google.com/maps/embed/v1/view?key=YOUR_GOOGLE_MAPS_API_KEY&center={},{}".format(lat,
                                                                                                                    lng)
        return False


class SpaceType(models.Model):
    _name = "space.type"
    _description = "Space Type"

    name = fields.Char('Name')


class LightingType(models.Model):
    _name = "lighting.type"
    _description = "Lighting Type"

    name = fields.Char('Name')


class FormatType(models.Model):
    _name = "format.type"
    _description = "Format Type"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)
