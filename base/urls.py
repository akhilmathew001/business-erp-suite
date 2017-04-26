#BASE URL Configuration

from django.conf.urls import url
from base.views import customer_views
from base.views import company_views


urlpatterns = [

    url(r'^customer/list$', customer_views.index_view, name='customer_list_view'),
    url(r'^customer/(?P<customer_id>[0-9]+)/form$', customer_views.form_view, name='customer_form_view'),
    url(r'^customer/(?P<customer_id>[0-9]+)/editCustomer$', customer_views.save_from_edit_view, name='edit_customer'),
    url(r'^customer/newCustomer$', customer_views.create_customer_template, name='customer_new_template'),
    url(r'^customer/createCustomer', customer_views.create_customer, name="create_new_customer"),
    url(r'^customer/(?P<customer_id>[0-9]+)/deleteCustomer$', customer_views.delete_customer, name='delete_customer'),
   
    url(r'^company/list$', company_views.company_list_view, name='company_list_view'),
    url(r'^company/(?P<company_id>[0-9]+)/form$',company_views.company_form_view, name="company_form_view"),
    url(r'^company/(?P<company_id>[0-9]+)/editCompany$', company_views.save_from_edit_view, name='edit_company'),
    url(r'^company/newCompany$', company_views.create_company_template, name='company_new_template'),
    url(r'^company/createCompany', company_views.create_company, name="create_new_company"),
    url(r'^company/(?P<company_id>[0-9]+)/deleteCompany$', company_views.delete_company, name='delete_company'),
    

]
