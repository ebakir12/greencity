# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class res_company(models.Model):
    _inherit = "res.company"

    sh_event_barcode_mobile_type = fields.Selection([
        ('sh_ebs_barcode','Barcode'),
        ('sh_er_qr_code','QR code'),        
        ('both','Both')
        ],default = 'sh_ebs_barcode', string='Ticket Scan Options In Mobile (vent)', translate=True)

    sh_event_bm_is_cont_scan = fields.Boolean(string='Continuously Scan?', translate=True)
    
    sh_event_bm_is_notify_on_success = fields.Boolean(string='Notification On Ticket Succeed?', translate=True)
    
    sh_event_bm_is_notify_on_fail = fields.Boolean(string='Notification On Ticket Failed?', translate=True)
        
    sh_event_bm_is_sound_on_success = fields.Boolean(string='Play Sound On Ticket Succeed?', translate=True)
    
    sh_event_bm_is_sound_on_fail = fields.Boolean(string='Play Sound On Ticket Failed?', translate=True)
            
