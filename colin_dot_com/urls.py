from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.list, name='list'),
    url(r'^$', views.index, name='index'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.show, name='show'),
    url(r'^products/add/$', views.add, name='add'),
    url(r'^products/(?P<product_url>.+)/$', views.show, name='show'),
    url(r'^companies/$', views.list_companies, name='list_companies'),
    url(r'^companies/(?P<company_id>[0-9]+)/$', views.show_company, name='show_company')
]
