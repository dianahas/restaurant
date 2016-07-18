from django.conf.urls import include, url

from . import views

urlpatterns = [
    #   /menu/  urls
    #url for adding a menu, web form
    url(r'^$', views.get_name, name='get_name'),
    #url to display all the menus
    url(r'^view-menu/$', views.view_menu , name='view-menu'),
    #url to display the "today" menus
    url(r'^view-daily/$', views.view_daily_menus , name='view-daily'),
    #url to display the orders for a specified menu
    url(r'^(?P<pk>[0-9]+)/$', views.getOrders, name='orders_by_menu'),

    
    #url(r'^menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
]	