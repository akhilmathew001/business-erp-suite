from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^login/$', views.login_user, name='login'),
    url(r'^loginBeforeView', views.login_before_view, name='login-before-view'),
    url(r'^redirectAfterLogin', views.redirect_after_login, name='redirect-after-login'),
    url(r'^signup/$', views.singnup, name='signup'),
    url(r'^login/identify/password=recover', views.forgot_password, name='forgot-password'),
    url(r'^logout/$', views.logout_user,  name='logout'),
    url(r'^home$', views.home_view , name='home'),
    url(r'^', views.get_home_or_login_view, name='index_view'),

]
