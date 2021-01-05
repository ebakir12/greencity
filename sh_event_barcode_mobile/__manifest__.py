# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
    "name": "Event Mobile Barcode Scanner | Event Mobile QRCode Scanner",

    "author" : "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",
    
    "support": "support@softhealer.com",    
        
    "version": "13.0.1",
        
    "category": "Sales",

    "summary": "Maintain Attendees QRCode, Reduce Fake Attendance App, Manage Event Ticket Barcode module, Scan Attendees event QR, Event Ticket Barcode Scanner, Event Ticket QRcode Scanner, Event Ticket Mobile Scanner, Event Badge QR Scanner Odoo",   
        
    "description": """Enhance your event security to protect against ticket duplication and costly fraud with real-time event Barcode or QRCode scanning with mobile. Event Barcode mobile scanner provides event venues with an efficient method of moving crowds through the entrances. Quickly scan tickets and get instant feedback with each ticket scanned. This module mainly used to scan the attendee's Barcode or QRCode on the ticket. In this module, there is mainly three validation for scanning a ticket. first of ticket must be in 'Confirm' state otherwise it will give warning, second is if you still scan the same ticket twice then it will give you a warning and the last is if there is any fake Barcode or QRCode on the ticket so it will give a warning.

 Event Ticket Mobile Barcode Scanner Odoo, Event Badge QR Scanner Odoo
 Scan Attendees QR Module, Scan Attendee Barcode In Mobile, Reduce Fake Attendance, Manage Event Ticket QRCode, Scan Attendees Event Barcode, Event Badge QR Scanner Odoo.
 Maintain Attendees QRCode, Reduce Fake Attendance App, Manage Event Ticket Barcode module, Scan Attendees event QR, Event Ticket Barcode Scanner, Event Badge QR Scanner Odoo """,
    
    "depends": [
            
                "event",
                "sh_event_reg_barcode_generator",
                "sh_event_reg_qr_generator",
                
            ],
    
    "data": [

        "views/asset.xml",
        "views/event_view.xml",
        "views/res_config_settings_views.xml",
        "reports/event_report.xml",

    ],    
    "images": ["static/description/background.png",],            
    "live_test_url": "https://youtu.be/uuEP3EajCxs",
    "installable": True,    
    "application": True,    
    "autoinstall": False,
    
    "price": 130,
    "currency": "EUR"        
}
