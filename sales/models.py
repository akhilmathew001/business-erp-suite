from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from base.models.customer import Customer
from crm.choices import sale_order_state,shipping_policy
# Create your models here.

class SaleOrder(models.Model):
    
    name = models.CharField('Subject',max_length=300,blank=False)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=False)
    origin = models.CharField('Source Document',max_length=50,blank=True)
    state = models.CharField('State',max_length=20,choices=sale_order_state,blank=True,default='draft')
    date_order = models.DateTimeField('Order date',blank=True)
    date_confirm =  models.DateField('Confirmation Date', readonly=True, select=True)
    sales_person = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, verbose_name='Sales Person')
    is_paid = models.BooleanField('Paid',default=False)
    is_delivered = models.BooleanField('Delivered',default=False)
    shipping_policy = models.CharField('Shipping Policy',max_length=50,choices=shipping_policy)