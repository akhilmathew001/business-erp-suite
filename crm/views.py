from django.shortcuts import render,get_object_or_404,Http404,HttpResponseRedirect
from crm.models.crm import CrmLead
from base.models.customer import Customer
from base.models.company import Company,State,Country
from django.views.decorators.cache import cache_control
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LeadForm
import pdb
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
            sales_persons = User.objects.all()
        except CrmLead.DoesNotExist:
            raise Http404('No lead found')
        else:
            context = {'lead':lead,'customers':customers,'companies':companies,'states':states,
                       'countries':countries,'sales_persons':sales_persons}
            return render(request,'crm/crm_lead_form_view.html',context)
    else:
        raise Http404('No Lead Specified')
    
@login_required    
def lead_save_from_edit_view(request,lead_id):
    if request.method == 'POST':
            try:
                lead = CrmLead.objects.get(pk=lead_id)
                customer = get_object_or_404(Customer,pk=request.POST['customer'])
                state = get_object_or_404(State,pk=request.POST['state'])
                country = get_object_or_404(Country,pk=request.POST['country'])
                sales_person = get_object_or_404(User,pk=request.POST['sales_person'])
            except CrmLead.DoesNotExist:
                raise Http404('Specified lead not found')
            except Customer.DoesNotExist:
                raise Http404('Selected customer doesnot exist or is not a valid one')
            else:        
                subject = request.POST['subject']
                stage = request.POST['stage']
                priority = request.POST['priority']
                email = request.POST['email']
                mobile = request.POST['mobile']
                fax = request.POST['fax']
                street = request.POST['street']
                street2 = request.POST['street2']
                city = request.POST['city']
                zip = request.POST['zip']
                lead = CrmLead(id=lead.id, subject=subject,customer=customer,stage=stage,priority=priority,email=email,mobile=mobile,fax=fax,street=street,
                           street2=street2,city=city,state=state,country=country,zip_code=zip,sales_person=sales_person)
                pdb.set_trace()
                lead.save()
                return HttpResponseRedirect(reverse('crm:lead_form_view',args=(lead.id,)))
    else:
        return render(request,'crm/crm_lead_list.html')

def create_lead_template(request):
    formObj = LeadForm()
    template = 'crm/crm_lead_new_form.html'
    context = {'form':formObj}
    return render(request,template,context)
    
    
def create_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            customer = form.cleaned_data['customer']
            stage = form.cleaned_data['stage']
            priority = form.cleaned_data['priority']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            fax = form.cleaned_data['fax']
            street = form.cleaned_data['street']
            street2 = form.cleaned_data['street2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']
            zip = form.cleaned_data['zip']
            sales_person = form.cleaned_data['sales_person']
            lead = CrmLead(subject=subject,customer=customer,stage=stage,priority=priority,email=email,mobile=mobile,fax=fax,street=street,
                           street2=street2,city=city,state=state,country=country,zip_code=zip,sales_person=sales_person)
            lead.save()
            return HttpResponseRedirect(reverse('crm:lead_form_view',args=(lead.id,)))
    else:
        formObj = LeadForm()
        template = 'crm/crm_lead_new_form.html'
        context = {'form':formObj}
    return render(request,template,context)

def delete_lead(request,lead_id):    
    try:
        lead = get_object_or_404(CrmLead,pk=lead_id)  
    except CrmLead.DoesNotExist:
        raise Http404('Lead does not exist')
    else:
        lead.delete()
        return HttpResponseRedirect(reverse('crm/crm_lead_list.html'))
    
    
    