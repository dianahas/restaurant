from django.conf.urls import url

from . import views

urlpatterns = [
    #   /api/  urls
    #url for sending all the menus for today.
    url(r'^menus/$', views.MenuList.as_view()),
    #url for operations with a menu like update,delete 
    url(r'^menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
    #url to see all the orders(GET)/ to add a new order (POST)
    url(r'^orders/$', views.OrderList.as_view()),
    #url to check the details of an order
    url(r'^code/$', views.orderByCode.as_view()),
    #url to set the rating to an update
    url(r'^rating/$', views.updateRating.as_view()),
]	