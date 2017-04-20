'''
Created on Apr 19, 2017

@author: Akhil Mathew
'''

from django import forms
from base.models.customer import Customer


class LeadForm(forms.Form):
    
    subject = forms.CharField(label='Subject', required=True)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),empty_label='Select customer')
