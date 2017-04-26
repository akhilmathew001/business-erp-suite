from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import pdb
import traceback
# Create your views here.

def get_index_or_login_view(request):
    return render(request, 'index/login.html')

def home_view(request):
    template_name = 'index/index.html'
    return render(request, template_name)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if username and password:
            try:
                user = User.objects.filter(username=username)
                #pdb.set_trace()
            except User.DoesNotExist:
                    error = traceback.format_exc()
                    raise Http404(error)
                    context = {'message':'User Not Found'}
                    template_name='index/login.html'
                    return render(request, template_name, context)
            else:
                if user:
                    #pdb.set_trace()
                    if user[0].check_password(password):
                        return HttpResponseRedirect(reverse('index:home')) 
                    else:
                        context = {'message':"User name and password don't match"}
                        template_name='index/login.html'
                        return render(request, template_name, context)
                else:
                    context = {'message':'User Not Found'}
                    template_name='index/login.html'
                    return render(request, template_name, context)
        else:
            context = {'message':'Enter username and password'}
            template_name='index/login.html'
            return render(request, template_name, context)        
    else:
        template_name='index/login.html'
        return render(request, template_name)      
            

def singnup(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = request.POST['regname']
        if email and user:
            extstngUser = User.objects.filter(username=user)
            password = request.POST['regpass']
            if extstngUser:
                context = {'message':'User already exist. Please try login'}
                template_name='index/login.html'
                return render(request, template_name, context)
            else:    
                newUser = User.objects.create_user(username=user, email=email, password=password)
                newUser.save()
                context = {'user_created':'User created'}
                return HttpResponseRedirect(reverse('index:login'))
        else:
            context = {'message':'Enter email, username and password to register'}
            template_name='index/login.html'
            return render(request, template_name, context)   
    else:
        template_name='index/login.html'
        return render(request, template_name)
    
def forgot_password(request):
    return HttpResponse('THIS FEATURE WILL BE ADDED SOON')    
    
    