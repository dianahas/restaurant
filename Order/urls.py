from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^new/(?P<pk>[0-9]+)/$', views.get_order, name='get_order'),
    url(r'^(?P<pk>[0-9]+)/$', views.updateStatus, name='order_sent'),
    url(r'^check_code/$', views.get_code, name='check_code'),
    url(r'^check_status/$', views.checkCode, name='check_status'),
]