# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    so_approval = fields.Boolean(
        string="Sale Order Approval",
        help="Enable this to require manager approval for sale orders above a set amount."
    )
    so_min_amount = fields.Monetary(
        string="Minimum Amount",
        help="Set the minimum amount to trigger double validation for sale orders requiring manager approval."
    )

    @api.model
    def get_values(self):
        """
            Override to retrieve custom field values from the 'ir.config_parameter' model.
         """
        res = super(ResConfigSettings, self).get_values()
        res['so_approval'] = self.env['ir.config_parameter'].sudo().get_param(
            "sales_order_approval.so_approval", default="")
        res['so_min_amount'] = self.env['ir.config_parameter'].sudo().get_param(
            "sales_order_approval.so_min_amount", default="")
        return res

    @api.model
    def set_values(self):
        """
            Override to set custom field values in the 'ir.config_parameter' model.
        """
        self.env['ir.config_parameter'].set_param(
            "sales_order_approval.so_approval",
            self.so_approval or '')
        self.env['ir.config_parameter'].set_param(
            "sales_order_approval.so_min_amount",
            self.so_min_amount or '')
        super(ResConfigSettings, self).set_values()
