from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.singnup, name='signup'),
    url(r'^login/identify/password=recover', views.forgot_password, name='forgot-password'),
    url(r'^home$', views.home_view , name='home'),
    url(r'^', views.get_index_or_login_view, name='index_view'),

]
