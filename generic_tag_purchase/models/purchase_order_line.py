# -*- coding: utf-8 -*-

from openerp import models


class PurchaseOrderLine(models.Model):
    _name = "purchase.order.line"
    _inherit = ["purchase.order.line",
                "generic.tag.mixin"]
