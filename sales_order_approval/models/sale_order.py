# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=
                             [('to_approve', 'To Approve'),
                              ('sent',)], ondelete={'to_approve': 'cascade'})

    def button_approve(self):
        """
            Method to approve the sale order and change its state to 'Sale'.
        """
        self.write({'state': 'sale'})

    def action_confirm(self):
        """
            Override to implement double validation logic based on company settings.
            Confirms the sale order if conditions are met; otherwise, sets the state to 'to_approve'.
        """
        res = super(SaleOrder, self).action_confirm()
        if self.company_id.so_double_validation:
            if self.env['ir.config_parameter'].sudo().get_param(
                    'sales_order_approval.so_approval'):
                if self.amount_total > float(
                        self.env['ir.config_parameter'].sudo().get_param(
                            'sales_order_approval.so_min_amount')):
                    if self.user_has_groups('sales_team.group_sale_manager'):
                        self.state = 'sale'
                    else:
                        self.state = 'to_approve'
        return res

    def action_cancel(self):
        """
            Method to cancel the sale order and update its state to 'cancel'.
        """
        self.state = 'cancel'
