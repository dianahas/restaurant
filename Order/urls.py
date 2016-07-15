from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.get_order, name='get_order'),
    url(r'^(?P<pk>[0-9]+)/$', views.updateStatus, name='order_sent'),
    url(r'^check_status/$', views.get_code, name='check_status'),
    url(r'^check_code/$', views.checkCode, name='check_code'),
]