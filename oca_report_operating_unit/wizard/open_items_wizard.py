# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class OpenItemsReportWizard(models.TransientModel):
    """Open items report wizard."""

    _inherit = "open.items.report.wizard"

    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit'
    )

    def _prepare_report_open_items(self):
        res = super(OpenItemsReportWizard, self)._prepare_report_open_items()
        if self.operating_unit_id:
            res['operating_unit_id'] = self.operating_unit_id.id
        return res

    # def _export(self, report_type):
    #     """Default export is PDF."""
    #     model = self.env['report_open_items_qweb']
    #     report = model.create(self._prepare_report_open_items())
    #     report.compute_data_for_report()
    #     return report.print_report(report_type)
