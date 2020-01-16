from django.conf.urls import url,include
from .views import (
	CreateView,
	ArtikelDetailView,
	ArtikelManageView,
	ArtikelUpdateView,
	ArtikelDeleteView,
	ArtikelListView,
	ArtikelKategoriListView,
	)

urlpatterns = [
    url(r'^create', CreateView.as_view(),name='create'),
    url(r'^detail/(?P<slug>[\w-]+)$',ArtikelDetailView.as_view(),name='detail'),
	url(r'^manage/$',ArtikelManageView.as_view(),name='manage'),
	url(r'^manage/update/(?P<pk>\d+)$',ArtikelUpdateView.as_view(),name='update'),
	url(r'^manage/delete/(?P<pk>\d+)$',ArtikelDeleteView.as_view(),name='delete'),
	url(r'^(?P<page>\d+)$',ArtikelListView.as_view(),name='list'),
	url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$',ArtikelKategoriListView.as_view(),name='category'),

]
