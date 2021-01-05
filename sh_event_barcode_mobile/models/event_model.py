# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.exceptions import Warning,UserError


class event_event(models.Model):
    _inherit = "event.event" 
    
    
    def default_sh_event_bm_is_cont_scan(self):
        if self.env.user and self.env.user.company_id:
            return self.env.user.company_id.sh_event_bm_is_cont_scan
    
    sh_event_barcode_mobile = fields.Char(string = "Mobile Barcode")
    
    sh_event_bm_is_cont_scan = fields.Char(string='Continuously Scan?',default = default_sh_event_bm_is_cont_scan, readonly=True)
        
    
    
    
    @api.onchange('sh_event_barcode_mobile')
    def _onchange_sh_event_barcode_mobile(self):
        
        if self.sh_event_barcode_mobile in ['',"",False,None]:
            return
        
        CODE_SOUND_SUCCESS = ""
        CODE_SOUND_FAIL = ""
        if self.env.user.company_id.sudo().sh_event_bm_is_sound_on_success:
            CODE_SOUND_SUCCESS = "SH_BARCODE_MOBILE_SUCCESS_"
        
        if self.env.user.company_id.sudo().sh_event_bm_is_sound_on_fail:
            CODE_SOUND_FAIL = "SH_BARCODE_MOBILE_FAIL_"    
            
                        
        
        if self:
            domain = []
            if self.env.user.company_id.sudo().sh_event_barcode_mobile_type == "sh_ebs_barcode":            
                domain = [("sh_ebs_barcode","=",self.sh_event_barcode_mobile)]
            
            elif self.env.user.company_id.sudo().sh_event_barcode_mobile_type == "sh_er_qr_code":            
                domain = [("sh_er_qr_code","=",self.sh_event_barcode_mobile)]
                
            elif self.env.user.company_id.sudo().sh_event_barcode_mobile_type == "both":            
                domain = ["|",
                    ("sh_ebs_barcode","=",self.sh_event_barcode_mobile),
                    ("sh_er_qr_code","=",self.sh_event_barcode_mobile)
                ]          
            
            reg = self.env['event.registration'].search(domain,limit = 1)
            if reg:
                if reg.state == 'done':
                    if self.env.user.company_id.sudo().sh_event_bm_is_notify_on_fail:    
                        message = _(CODE_SOUND_FAIL + 'Registration(%s) already attended')  %(reg.partner_id.name if reg.partner_id else '')                 
                        self.env['bus.bus'].sendone(
                            (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
                            {'type': 'simple_notification', 'title': _('Alert'), 'message': message, 'sticky': False, 'warning': True})
                    
                    return
                                         
                
                if reg.state != 'open':
                    if self.env.user.company_id.sudo().sh_event_bm_is_notify_on_fail:    
                        message = _(CODE_SOUND_FAIL + 'Scanned attendee(%s) not in Confirmed state') %(reg.partner_id.name if reg.partner_id else '')                                        
                        self.env['bus.bus'].sendone(
                            (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
                            {'type': 'simple_notification', 'title': _('Failed'), 'message': message, 'sticky': False, 'warning': True})
                    return
                                
                    
                # confirm attendee
                reg.button_reg_close()
                
                if self.env.user.company_id.sudo().sh_event_bm_is_notify_on_success:
                    message = _(CODE_SOUND_SUCCESS + 'Registration(%s) attended successfully') %(reg.partner_id.name if reg.partner_id else '')
                    self.env['bus.bus'].sendone(
                        (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
                        {'type': 'simple_notification', 'title': _('Succeed'), 'message': message, 'sticky': False, 'warning': False})
                return
               
                          
            else:
                if self.env.user.company_id.sudo().sh_event_bm_is_notify_on_fail:    
                    message = _(CODE_SOUND_FAIL + 'Scanned QR Code/Barcode not exist in any attendee!')                  
                    self.env['bus.bus'].sendone(
                        (self._cr.dbname, 'res.partner', self.env.user.partner_id.id),
                        {'type': 'simple_notification', 'title': _('Failed'), 'message': message, 'sticky': False, 'warning': True})




