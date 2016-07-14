from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.get_order, name='get_order'),
    url(r'^(?P<pk>[0-9]+)/$', views.updateStatus, name='order_sent'),
]