'''
Created on Apr 19, 2017

@author: Akhil Mathew
'''

from django import forms
from base.models.customer import Customer
from base.models.company import State,Country
from django.contrib.auth.models import User


class LeadForm(forms.Form):
    
    stage_choice = [('new','New'),('progress','In progress'),('matured','Matured'),('dead','Dead')]
    priority_choice = [('low','Low'),('normal','Normal'),('high','High'),('veryhigh','Very High')]
    
    subject = forms.CharField(label='Subject', required=True)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),empty_label='Select customer',label='Customer')
    stage = forms.ChoiceField(label='Stage',choices=stage_choice)
    priority = forms.ChoiceField(label='Priority',choices=priority_choice)
    email = forms.EmailField(label='Email')
    mobile = forms.IntegerField(label='Mobile')
    fax = forms.IntegerField(label='Fax')
    street = forms.CharField(label='Street')
    street2 = forms.CharField(label='Lane')
    city = forms.CharField(label='City')
    state = forms.ModelChoiceField(queryset=State.objects.all(),empty_label='Select state',label='State')
    country = forms.ModelChoiceField(queryset=Country.objects.all(),empty_label='Select country', label='Country')
    zip = forms.IntegerField(label='Zip code')
    sales_person = forms.ModelChoiceField(queryset=User.objects.all(),empty_label='Select sales person',label='Sales person')