from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from base.models.customer import Customer
from base.models.company import State,Country,Company
from django.views.decorators.cache import cache_control
import traceback
from pip.cmdoptions import no_cache
# Create your views here.

   ## CUSTOMER

def index_view(request):
    customers = Customer.objects.all()
    context = {'customer_list':customers}
    template = 'base/customer_list_view.html'
    return render(request,template,context)

@cache_control(no_cache=True, must_revalidate=True)
def form_view(request,customer_id):
    if customer_id:
        try:
            customer = get_object_or_404(Customer,pk=customer_id)
            states = State.objects.all()
            countries = Country.objects.all()
            companies = Company.objects.all()
            context = {'customer_obj':customer,'states':states,'countries':countries,'companies':companies}
        except Customer.DoesNotExist:
            raise Http404('Customer does not exist')
        else:    
            return render(request, 'base/customer_form_view.html', context)
    else:
        raise Http404('Customer ID not specified')


def save_from_edit_view(request,customer_id):
    if request.method == 'POST':
        try:
            customer_name = request.POST['customer_name']
            is_company = request.POST.get('is_company', False)
            customer_email = request.POST['customer_email']
            customer_mobile = request.POST['customer_mobile']
            customer_street = request.POST['customer_street']
            customer_street2 = request.POST['customer_street2']
            customer_city = request.POST['customer_city']
            customer_state = request.POST['customer_state']
            customer_country = request.POST['customer_country']
            if is_company:
                customer_company = request.POST['customer_company']
            else:
                customer_company = None
            customer_note = request.POST['customer_note']
        except Exception:
            tb = traceback.format_exc()
            print tb
            raise Http404(tb)
        else:
            try:
                if customer_state == 'none':
                    state_obj = None
                else:
                    state_obj = get_object_or_404(State, pk=customer_state)
                if customer_country == 'none':
                    country_obj = None
                else:
                    country_obj = get_object_or_404(Country, pk=customer_country)
                if customer_company == None:
                    company = None
                else:
                    company = get_object_or_404(Company, pk=customer_company)
            except (State.DoesNotExist, Country.DoesNotExist, Company.DoesNotExist):
                tb = traceback.format_exception()
                raise Http404('Error %s',tb)
            else:
                obj = Customer(id=customer_id,name=customer_name,is_company=is_company,company=company,mobile=customer_mobile,email=customer_email,
                     street=customer_street,street2=customer_street2,city=customer_city,state=state_obj,country=country_obj,note=customer_note)
                obj.save()

                return HttpResponseRedirect(reverse('base:customer_form_view',args=(customer_id)))
            
            
def create_customer_template(request):
    states = State.objects.all()
    countries = Country.objects.all()
    companies = Company.objects.all()
    template = 'base/customer_new_form.html'
    return render(request, template_name=template,context={'companies':companies,'states':states,'countries':countries})      


def create_customer(request):     
    if request.method == 'POST':
        try:
            customer_name = request.POST['customer_name']
            is_company = request.POST.get('is_company', False)
            customer_email = request.POST['customer_email']
            customer_mobile = request.POST['customer_mobile']
            customer_street = request.POST['customer_street']
            customer_street2 = request.POST['customer_street2']
            customer_city = request.POST['customer_city']
            customer_state = request.POST['customer_state']
            customer_country = request.POST['customer_country']
            if is_company:
                customer_company = request.POST['customer_company']
            else:
                customer_company = None
            customer_note = request.POST['customer_note']
        except Exception:
            tb = traceback.format_exc()
            print tb
            raise Http404(tb)
        else:
            try:
                if customer_state == 'none':
                    state_obj = None
                else:
                    state_obj = get_object_or_404(State, pk=customer_state)
                if customer_country == 'none':
                    country_obj = None
                else:
                    country_obj = get_object_or_404(Country, pk=customer_country)
                if customer_company == None:
                    company = None
                else:
                    company = get_object_or_404(Company, pk=customer_company)
            except (State.DoesNotExist, Country.DoesNotExist, Company.DoesNotExist):
                tb = traceback.format_exception()
                raise Http404('Error %s',tb)
            else:
                obj = Customer(name=customer_name,is_company=is_company,company=company,mobile=customer_mobile,email=customer_email,
                     street=customer_street,street2=customer_street2,city=customer_city,state=state_obj,country=country_obj,note=customer_note)
                obj.save()
                customer_id = obj.pk
                return HttpResponseRedirect(reverse('base:customer_form_view',args=(customer_id,)))
            
            
@cache_control(no_cache=True, must_revalidate=True)         
def delete_customer(request,customer_id):
    try:
        customer = get_object_or_404(Customer,pk=customer_id)  
    except Customer.DoesNotExist:
        raise Http404('Customer does not exist')
    else:
        customer.delete()
        return HttpResponseRedirect(reverse('base:customer_list_view'))
    
    
    
        
    
    
    
    
    
    
    
    
                  
            
