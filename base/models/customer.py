from __future__ import unicode_literals

from django.db import models
from base.models.company import State,Country,Company


# Create your models here.

class Customer(models.Model):

    name = models.CharField('Customer',max_length=250, blank=False)
    image = models.ImageField('Image',blank=True, max_length=500)
    is_company = models.BooleanField('Is comapany', blank=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Company')
    mobile = models.BigIntegerField('Mobile', blank=True)
    email = models.EmailField('Email', blank=True)
    street = models.CharField('Lane',max_length=300, blank=True)
    street2 = models.CharField('Street',max_length=300, blank=True)
    city = models.CharField('City',max_length=250, blank=True)
    state = models.ForeignKey(State, verbose_name='State',blank=True, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, verbose_name='Country',blank=True, on_delete=models.CASCADE ,null=True)
    note = models.TextField('Internal Note',blank=True)
    date_create = models.DateTimeField(auto_now_add=True,null=True)


    def __unicode__(self):
        return self.name
