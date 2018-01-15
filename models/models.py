# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import base64
import barcode
from barcode.writer import ImageWriter
from PIL import Image

class ProductTemplate(models.Model):

    _inherit = "product.template"
    barcode_image = fields.Binary("Code-barre", attachment=True, help="Image du code-barre")
    
    @api.depends('barcode')
    @api.onchange('barcode')
    def _generate_bacode_image(self):
        for record in self:
            
            barcode_image = record.barcode_image
            
            barcode_odoo = record.barcode
            ean = barcode.get('ean13', barcode_odoo, writer=ImageWriter())
            filename = ean.save('ean13')
            
            f = open("ean13.png")
            filename = base64.encodestring(f.read())
            f.close()
            
            record.barcode_image = filename

    @api.depends('barcode')
    def generate_bacode(self):
        ptmp = self.env['product.template']
        products = ptmp.search([('barcode','=ilike','2%')]).sorted(key=lambda r: r.barcode)
        last = len(products)-1
        lastBarcode = products[last].barcode[0:-1]
        
        for record in self:
            newBarcode = str(int(lastBarcode) + 1)
            record.barcode = newBarcode
            secure = self._calc_security_code()
            record.barcode += str(secure)
            self._generate_bacode_image()
            
    @api.depends('barcode')
    def _calc_security_code(self):
        barcode = self.barcode
        #step 1 : addition of pair index from pos 1 of the barcode
        step1 = 0
        for index in (1, 3, 5,7,9,11):
            step1 += int(barcode[index])
        
        #step2 : step1 * 3
        step2 = step1 * 3
        
        #step3 : addition of impair index from pos 0 of the barcode
        step3 = 0
        for index in (0,2,4,6,8,10):
            step3 += int(barcode[index])
        
        #step4 : step2 + step3
        step4 = step2 + step3
        
        #step5 : smaller added number that give 10 multiplier
        founded = False
        incr = 0
        while founded == False:
            number = step4 + incr
            if number%10 == 0:
                step5=incr
                founded = True
            else:
                incr += 1
                
        return step5