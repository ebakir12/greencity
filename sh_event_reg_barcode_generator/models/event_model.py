# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models, fields, api, _
from odoo.exceptions import Warning,UserError

import math
import re

import werkzeug
import werkzeug.exceptions
import base64


class event_registration(models.Model):
    _inherit = 'event.registration'

    sh_ebs_barcode = fields.Char(string = "Barcode", readonly = True)
    sh_ebs_barcode_img = fields.Binary(string = "Barcode Image", readonly = True)    
    
    def _check_auto_confirmation(self):
        
        for registration in self:

            ean = generate_ean(str(registration.id))
            registration.sh_ebs_barcode = ean
             
            #Generate Barcode Image.
            try:
                barcode = self.env['ir.actions.report'].barcode('EAN13', ean, width=500, height=90, humanreadable=0)
                if barcode:
                    registration.sh_ebs_barcode_img = base64.b64encode(barcode)
                     
            except (ValueError, AttributeError):
                raise werkzeug.exceptions.HTTPException(description='Cannot convert into barcode.')        
             
                
        return super(event_registration,self)._check_auto_confirmation()
         
    
#     @api.model
#     def create(self, vals):
#         res = super(event_registration, self).create(vals)
#         ean = generate_ean(str(res.id))
#         res.sh_ebs_barcode = ean
#         
#         #Generate Barcode Image.
#         try:
#             barcode = self.env['ir.actions.report'].barcode('EAN13', ean, width=500, height=90, humanreadable=0)
#             if barcode:
#                 res.sh_ebs_barcode_img = base64.b64encode(barcode)
#                 
#         except (ValueError, AttributeError):
#             raise werkzeug.exceptions.HTTPException(description='Cannot convert into barcode.')        
#         
#         return res




def ean_checksum(eancode):
    """returns the checksum of an ean string of length 13, returns -1 if
    the string has the wrong length"""
    if len(eancode) != 13:
        return -1
    oddsum = 0
    evensum = 0
    eanvalue = eancode
    reversevalue = eanvalue[::-1]
    finalean = reversevalue[1:]

    for i in range(len(finalean)):
        if i % 2 == 0:
            oddsum += int(finalean[i])
        else:
            evensum += int(finalean[i])
    total = (oddsum * 3) + evensum

    check = int(10 - math.ceil(total % 10.0)) % 10
    return check


def check_ean(eancode):
    """returns True if eancode is a valid ean13 string, or null"""
    if not eancode:
        return True
    if len(eancode) != 13:
        return False
    try:
        int(eancode)
    except:
        return False
    return ean_checksum(eancode) == int(eancode[-1])


def generate_ean(ean):
    """Creates and returns a valid ean13 from an invalid one"""
    if not ean:
        return "0000000000000"
    ean = re.sub("[A-Za-z]", "0", ean)
    ean = re.sub("[^0-9]", "", ean)
    ean = ean[:13]
    if len(ean) < 13:
        ean = ean + '0' * (13 - len(ean))
    return ean[:-1] + str(ean_checksum(ean))
