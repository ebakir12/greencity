# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import api, fields, models


class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    sh_event_barcode_mobile_type = fields.Selection([
        ('sh_ebs_barcode','Barcode'),
        ('sh_er_qr_code','QR code'),        
        ('both','Both')
        ],related='company_id.sh_event_barcode_mobile_type', string='Ticket Scan Options In Mobile (vent)', translate=True,readonly = False)


    sh_event_bm_is_cont_scan = fields.Boolean(related='company_id.sh_event_bm_is_cont_scan', string='Continuously Scan?', translate=True,readonly = False)
    
    sh_event_bm_is_notify_on_success = fields.Boolean(related='company_id.sh_event_bm_is_notify_on_success',string='Notification On Ticket Succeed?', translate=True,readonly = False)
    
    sh_event_bm_is_notify_on_fail = fields.Boolean(related='company_id.sh_event_bm_is_notify_on_fail',string='Notification On Ticket Failed?', translate=True,readonly = False)
    
    sh_event_bm_is_sound_on_success = fields.Boolean(related='company_id.sh_event_bm_is_sound_on_success', string='Play Sound On Ticket Succeed?', translate=True, readonly = False)
    
    sh_event_bm_is_sound_on_fail = fields.Boolean(related='company_id.sh_event_bm_is_sound_on_fail', string='Play Sound On Ticket Failed?', translate=True, readonly = False)
        
