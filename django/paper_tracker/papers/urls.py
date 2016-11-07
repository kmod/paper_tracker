from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^papers$', views.papers_index, name='papers_index'),
    url(r'^collections$', views.collections_index, name='collections_index'),
    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection, name='collection'),
]
