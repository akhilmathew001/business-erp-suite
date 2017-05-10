'''
Created on May 10, 2017

@author: Akhil Mathew
'''

from django import forms
from base.models.company import Company, State, Country

class CustomerForm(forms.Form):
    
    name = forms.CharField(label='Customer',max_length=250, required=True)
    image = forms.ImageField(label='Image')
    is_company = forms.BooleanField(label='Is comapany')
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label='Select company', label='Company')
    mobile = forms.IntegerField(label='Mobile')
    email = forms.EmailField(label='Email')
    street = forms.CharField(label='Lane',max_length=300)
    street2 = forms.CharField(label='Street',max_length=300)
    city = forms.CharField(label='City',max_length=250)
    state = forms.ModelChoiceField(queryset=State.objects.all(), empty_label='Select state', label='State')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Select country' ,label='Country')
    note = forms.CharField(label='Internal Note',widget=forms.Textarea)
    date_create = forms.DateTimeField()
