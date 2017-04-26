from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^lead/list$', views.leads_list_view, name='leads_list_view'),
    url(r'^lead/(?P<lead_id>[0-9]+)/form$', views.lead_form_view,  name='lead_form_view'),
    url(r'^lead/(?P<lead_id>[0-9]+)/editLead$', views.lead_save_from_edit_view, name='edit_lead'),
    url(r'lead/newLead', views.create_lead_template, name='new_lead_template'),
    url(r'lead/createLead', views.create_lead, name='create_new_lead'),
    url(r'^lead/(?P<lead_id>[0-9]+)/deleteLead', views.delete_lead, name='delete_lead'),
    
    
    
]