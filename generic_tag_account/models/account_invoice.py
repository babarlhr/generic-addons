# -*- coding: utf-8 -*-
from openerp import models


class AccountInvoice(models.Model):
    _name = "account.invoice"
    _inherit = ["account.invoice",
                "generic.tag.mixin"]