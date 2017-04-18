from __future__ import unicode_literals

from django.db import models

#create models here

class Country(models.Model):
    name = models.CharField('Name',max_length=250, blank=False)

    def __unicode__(self):
        return self.name

class State(models.Model):
    name = models.CharField('State',max_length=250, blank=False)

    def __unicode__(self):
        return self.name


class Company(models.Model):

    name = models.CharField('Company',max_length=250, blank=False)
    mobile = models.BigIntegerField('Mobile', blank=True)
    phone = models.BigIntegerField('Phone', blank=True)
    email = models.EmailField('Email', blank=True)
    street = models.CharField('Lane',max_length=300, blank=True)
    street2 = models.CharField('Street',max_length=300, blank=True)
    city = models.CharField('City',max_length=250, blank=True)
    state = models.ForeignKey(State, verbose_name='State', blank=True, on_delete=models.CASCADE ,null=True)
    country = models.ForeignKey(Country, verbose_name='Country', blank=True, on_delete=models.CASCADE ,null=True)
    note = models.TextField('Internal Note', blank=True)
    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __unicode__(self):
        return self.name
