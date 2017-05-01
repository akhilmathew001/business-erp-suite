'''
Created on Apr 25, 2017

@author: Akhil Mathew
'''
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from crm.choices import unit_choice,product_type_choices,status

class ProductUOM(models.Model):
    
    
    name = models.CharField('Unit of measure', max_length=50,blank=False)
    unit = models.CharField('Unit category',max_length=50,choices=unit_choice)
    
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField('Product Name',max_length=300,blank=False)
    sell_ok = models.BooleanField('Can be sold')
    purchase_ok = models.BooleanField('Can be purchased')
    image = models.ImageField(blank=True)
    product_type = models.CharField('Product Type',max_length=12,choices=product_type_choices,blank=True)
    product_uom = models.ForeignKey(ProductUOM,on_delete=models.CASCADE,blank=True,null=True)
    sale_price = models.FloatField('Sale Price',blank=True)
    cost_price = models.FloatField('Cost Price',blank=True) 
    product_status = models.CharField('Status',max_length=10,choices=status,blank=True)
    description = models.TextField('Product Description')
    quantity_on_hand = models.IntegerField('Quantity On Hand',blank=True)
    product_manager = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Product Manager')
    rack = models.CharField('Rack',max_length=100, blank=True)
    row = models.CharField('Row',max_length=100, blank=True)
    case = models.CharField('Case',max_length=100, blank=True)
    warranty = models.DurationField('Warranty',blank=False)
    lead_time = models.DurationField('Customer Lead TIme',blank=False)
    description_purchase = models.TextField('Purchase Description')
    description_sale = models.TextField('Sales Description')
    
    
    def __unicode__(self):
        return self.name
    
    
    
