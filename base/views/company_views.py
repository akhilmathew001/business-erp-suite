from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from base.models.company import State,Country,Company
from django.views.decorators.cache import cache_control
import traceback
# Create your views here.

	## COMPANY ##

@cache_control(no_cache=True, must_revalidate=True)
def company_list_view(request):
	companies = Company.objects.all()
	template = 'base/company_list_view.html'
	context = {'company_list':companies}
	return render(request, template, context)


@cache_control(no_cache=True, must_revalidate=True)
def company_form_view(request, company_id):
	if company_id:
		try:
			company = get_object_or_404(Company,pk=company_id)
			states = State.objects.all()
			countries = Country.objects.all()
			context = {'company_obj':company,'states':states,'countries':countries}
		except Company.DoesNotExist:
			raise Http404('Company does not exist')
		return render(request, 'base/company_form_view.html',context)
	else:
		raise Http404('Company ID not specified')

@cache_control(no_cache=True, must_revalidate=True)	
def save_from_edit_view(request,company_id):
	if request.method == 'POST':
		try:
			company_name = request.POST['company_name']
			company_email = request.POST['company_email']
			company_mobile = request.POST['company_mobile']
			company_phone = request.POST['company_phone']
			company_street = request.POST['company_street']
			company_street2 = request.POST['company_street2']
			company_city = request.POST['company_city']
			company_state = request.POST['company_state']
			company_country = request.POST['company_country']
		except Exception:
			tb = traceback.format_exc()
			print tb
			raise Http404(tb)
		else:
			try:
				if company_state == 'none':
					state_obj = None
				else:
					state_obj = get_object_or_404(State,pk=company_state)	
				if company_country == 'none':
					country_obj = None
				else:	
					country_obj = get_object_or_404(Country, pk=company_country)	
			except (State.DoesNotExist, Country.DoesNotExist):
					tb = traceback.format_exc()
					raise Http404(tb)
			else:
				obj = Company(id=company_id,name=company_name,mobile=company_mobile,email=company_email,phone=company_phone,
						street=company_street,street2=company_street2,city=company_city,state=state_obj,country=country_obj)
				try:
					#pdb.set_trace()
					obj.save()
				except Exception as E:		
					tb = traceback.format_exc()
					print tb
					raise Http404(tb)
				
				return HttpResponseRedirect(reverse('base:company_form_view',args=(company_id,)))


def create_company_template(request):
	states = State.objects.all()
	countries = Country.objects.all()
	template = 'base/company_new_form.html'
	return render(request, template_name=template,context={'states':states,'countries':countries})


def create_company(request):
	if request.method == 'POST':
		try:
			company_name = request.POST['company_name']
			company_email = request.POST['company_email']
			company_mobile = request.POST['company_mobile']
			company_phone = request.POST['company_phone']
			company_street = request.POST['company_street']
			company_street2 = request.POST['company_street2']
			company_city = request.POST['company_city']
			company_state = request.POST['company_state']
			company_country = request.POST['company_country']
		except Exception:
			tb = traceback.format_exc()
			print tb
			raise Http404(tb)
		else:
			try:
				if company_state == 'none':
					state_obj = None
				else:
					state_obj = get_object_or_404(State,pk=company_state)	
				if company_country == 'none':
					country_obj = None
				else:	
					country_obj = get_object_or_404(Country, pk=company_country)	
			except (State.DoesNotExist, Country.DoesNotExist):
					tb = traceback.format_exc()
					raise Http404(tb)
			else:
				obj = Company(name=company_name,mobile=company_mobile,email=company_email,phone=company_phone,
						street=company_street,street2=company_street2,city=company_city,state=state_obj,country=country_obj)
				obj.save()	
				company_id = obj.pk
				return HttpResponseRedirect(reverse('base:company_form_view',args=(company_id,)))
			
@cache_control(no_cache=True, must_revalidate=True)
def delete_company(request, company_id):
	try:
		company = get_object_or_404(Company, pk=company_id)  
	except Company.DoesNotExist:    
		raise Http404('Company not found..!')
	else:
		company.delete()
		return HttpResponseRedirect(reverse('base:company_list_view'))


