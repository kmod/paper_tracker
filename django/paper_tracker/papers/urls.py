from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^papers$', views.papers_index, name='papers_index'),
    url(r'^$', views.collections_index, name='collections_index'),
    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection, name='collection'),
    url(r'^paper/new$', views.paper_new, name='paper_new'),
    # url(r'^paper/(?P<paper_id>[0-9]+)$', views.paper, name='paper'),
    url(r'^paper/(?P<paper_id>[0-9]+)/find_pdf$', views.paper_findpdf, name='paper_findpdf'),
    url(r'^paper/(?P<paper_id>[0-9]+)/delete$', views.paper_delete, name='paper_delete'),
    url(r'^collection/(?P<collection_id>[0-9]+)/edit/(?P<paper_id>[0-9]+)$', views.cpaper, name='cpaper'),
]
