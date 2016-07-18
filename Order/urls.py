from django.conf.urls import include, url

from . import views

urlpatterns = [
	#   /order/  urls
	#url for adding an order, web form, after choosing the menu
    url(r'^new/(?P<pk>[0-9]+)/$', views.get_order, name='get_order'),
    #url to the form where you see the orders associated with a menu
    url(r'^(?P<pk>[0-9]+)/$', views.updateStatus, name='order_sent'),
    #url to the form where the order status is checked
    url(r'^check_code/$', views.get_code, name='check_code'),
    #url  for the page where is displayed the order details.
    url(r'^check_status/$', views.checkCode, name='check_status'),
]