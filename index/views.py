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
                pdb.set_trace()
            except User.DoesNotExist:
                    error = traceback.format_exc()
                    raise Http404(error)
                    context = {'message':'User Not Found'}
                    template_name='index/login.html'
                    return render(request, template_name, context)
            else:
                if user:
                    if user.check_password(password):
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
        password = request.POST['regpass']
        newUser = User.objects.create_user(username=user, email=email, password=password)
        newUser.save()
        pdb.set_trace()
        return HttpResponseRedirect(reverse('index:login'))
    else:
        return Http404('Error')