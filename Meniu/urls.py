from django.conf.urls import include, url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.get_name, name='get_name'),
    url(r'^view-menu/$', views.view_menu , name='view-menu'),
    url(r'^view-daily/$', views.view_daily_menus , name='view-daily'),
    url(r'^(?P<pk>[0-9]+)/$', views.getOrders, name='orders_by_menu'),
    #url(r'^menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
]	