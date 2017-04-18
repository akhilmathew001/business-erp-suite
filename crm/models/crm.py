from __future__ import unicode_literals

from django.db import models
from base.models.customer import Customer
from base.models.company import Company,Country,State
from django.contrib.auth.models import User
from datetime import datetime



class CrmLead(models.Model):

    stage_choice = [('new','New'),('dead','Dead')]
    priority_choice = [('low','Low'),('normal','Normal'),('high','High'),('veryhigh','Very High')]

    subject = models.CharField('Subject',max_length=300,blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer',blank=False)
    stage = models.CharField('Stage',choices=stage_choice, max_length=5, blank=False, default='new')
    priority = models.CharField('Priority',choices=priority_choice, max_length=10,default='normal')
    email = models.EmailField('Email',blank=True)
    mobile = models.BigIntegerField('Mobile',blank=True)
    fax = models.IntegerField('Fax',blank=True, null=True)
    street = models.CharField('Lane',max_length=300, blank=True)
    street2 = models.CharField('Street', max_length=250, blank=True)
    city = models.CharField('City', max_length=250, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='State', blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    zip_code = models.SmallIntegerField('Zip Code', blank=True, null=True)
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Sales Person', blank=True, null=True)
    date_create = models.DateTimeField('Date created',auto_now_add=True, null=True)



    def __unicode__(self):
        return self.subject
