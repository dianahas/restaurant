from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menus/$', views.MenuList.as_view()),
    url(r'^menus/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),
    url(r'^orders/$', views.OrderList.as_view()),
    url(r'^code/$', views.orderByCode.as_view()),
    url(r'^rating/$', views.updateRating.as_view()),
]	