from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^', views.get_index_view, name='index_view'),
    url(r'^home/$', views.get_index_view , name='home'),

]
