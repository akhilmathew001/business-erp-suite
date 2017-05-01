'''
Created on Apr 19, 2017

@author: Akhil Mathew
'''

from django import forms
from base.models.customer import Customer
from base.models.company import State,Country
from crm.models.product import Product
from django.contrib.auth.models import User
from crm.choices import priority_choice,stage_choice


class LeadForm(forms.Form):
    
    subject = forms.CharField(label='Subject', required=True)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),empty_label='Select customer',label='Customer')
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(),label='Products')
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
    

class ProductForm(forms.Form):
    
    producut_type_choices = [('stockable','Stockable'),('consumable','Consumable'),('service','Service')]
    status = [('development','In developemt'),('normal','Normal'),('end','End of Life Cycle'),('obsolete','Obsolote')]
    
    image = forms.ImageField()
    name = forms.CharField(label='Product Name',max_length=300,required=True)
    sell_ok = forms.BooleanField(label='Can be sold')
    purchase_ok = forms.BooleanField(label='Can be purchased')
    product_type = forms.ChoiceField(label='Product Type', choices=producut_type_choices)
    sale_price = forms.FloatField(label='Sale Price')
    cost_price = forms.FloatField(label='Cost Price') 
    product_status = forms.ChoiceField(label='Status',choices=status)
    description = forms.CharField(label='Product Description',widget=forms.Textarea)
    quantity_on_hand = forms.IntegerField(label='Quantity On Hand')
    product_manager = forms.ModelChoiceField(queryset=User.objects.all(),empty_label='Select product manager'
                                             ,label='Product Manager')
    rack = forms.CharField(label='Rack')
    row = forms.CharField(label='Row')
    case = forms.CharField(label='Case')
    warranty = forms.DurationField(label='Warranty')
    lead_time = forms.DurationField(label='Customer Lead TIme')
    description_purchase = forms.CharField(label='Purchase Description',widget=forms.Textarea)
    description_sale = forms.CharField(label='Sales Description',widget=forms.Textarea)
    
        