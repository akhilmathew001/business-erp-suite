from django.shortcuts import render,get_object_or_404,Http404,HttpResponseRedirect
from crm.models.crm import CrmLead
from base.models.customer import Customer
from base.models.company import Company,State,Country
from django.views.decorators.cache import cache_control
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def leads_list_view(request):
    leads = CrmLead.objects.all()
    template_name = 'crm/crm_lead_list.html'
    context = {'crm_leads':leads}
    return render(request, template_name, context)


@cache_control(no_cache=True, must_validate=True)
def lead_form_view(request,lead_id):
    if lead_id:
        try:
            lead = get_object_or_404(CrmLead,pk=lead_id)
            customers = Customer.objects.all()
            companies = Company.objects.all()
            states = State.objects.all()
            countries = Country.objects.all()
        except CrmLead.DoesNotExist:
            raise Http404('No lead found')
        else:
            context = {'lead':lead,'customers':customers,'companies':companies,'states':states,'countries':countries}
            return render(request,'crm/crm_lead_form_view.html',context)
    else:
        raise Http404('No Lead Specified')
    
@login_required    
def lead_save_from_edit_view(request,lead_id):
    pass

def create_lead_template(request):
    pass

def create_lead(request):
    pass

def delete_lead(request,lead_id):    
    pass