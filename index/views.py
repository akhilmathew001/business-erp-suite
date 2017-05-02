from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
import pdb
import traceback
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
# Create your views here.
#nextmedialabs.com nextmedia.io 

@login_required(login_url='/loginBeforeView')
def get_home_or_login_view(request):
    #pdb.set_trace()
    if request.user.is_authenticated():
        return render(request, 'index/index.html')
    else:
        return render(request, 'index/login.html')

@login_required(login_url='/loginBeforeView')
def home_view(request):
    template_name = 'index/index.html'
    return render(request, template_name)

def login_before_view(request):
    template = 'index/login_before_view.html'
    return render(request, template)

def redirect_after_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    redirectTO = request.POST['next']
                    login(request, user)
                    return HttpResponseRedirect(redirectTO)
                else:
                    template = 'index/login_before_view.html'
                    context = {'message':"This is a disabled user account, You can't login"}
                    return render(request, template, context)
            if user is None:
                template = 'index/login_before_view.html'
                context = {'message':'No user found!'}
                return render(request, template, context)
                
        else:
            template = 'index/login_before_view.html'
            context = {'message':'Enter username and password to login'}
            return render(request, template, context)
    else:
        template = 'index/login_before_view.html'
        return render(request, template)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        if username and password:
            user = authenticate(username=username,password=password)
            #pdb.set_trace()
            if user is None:
                check = User.objects.filter(username=username)
                try:
                    if check[0]:
                        context = {'message':"User name and password has no match"}
                        template_name='index/login.html'
                        return render(request, template_name, context)
                except IndexError:
                    context = {'message':'User Not Found'}
                    template_name='index/login.html'
                    return render(request, template_name, context)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index:home'))
                else:
                    context = {'message':"This is a disabled user account, You can't login"}
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
    template_response = auth_views.password_change(request)
    return template_response    
    
def logout_user(request):
    logout(request)
    context = {'message':'You have succesfully logged out...'}
    template_name='index/login.html'
    return render(request, template_name, context) 
       