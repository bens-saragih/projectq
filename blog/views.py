from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,TemplateView
from .models import Artikel
from .forms import ArtikelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

	### Penulis ###

class CreateView(UserPassesTestMixin,CreateView):
	template_name = 'blog/create.html'
	form_class = ArtikelForm
	raise_exception = True

	
	def test_func(self):
	    return self.request.user.groups.filter(name='penulis').exists() 
	
	


	#### Editor User ####

class ArtikelManageView(UserPassesTestMixin,ListView):
	model = Artikel 
	template_name = 'blog/artikel_manage.html'
	context_object_name = 'artikel_list'
	raise_exception = True

	def test_func(self):
	    return self.request.user.groups.filter(name='editor').exists() 

class ArtikelDeleteView(UserPassesTestMixin,DeleteView):
	model = Artikel 
	template_name = 'blog/artikel_delete_confirmation.html'
	success_url = reverse_lazy('blog:manage')
	raise_exception = True

	def test_func(self):
	    return self.request.user.groups.filter(name='editor').exists() 

class ArtikelUpdateView(UserPassesTestMixin,UpdateView):
	login_url = None
	form_class = ArtikelForm 
	model = Artikel 
	template_name = 'blog/artikel_update.html'
	raise_exception = True

	def test_func(self):
	    return self.request.user.groups.filter(name='editor').exists() 


	#### View ####

class ArtikelDetailView(DetailView):
	model = Artikel 
	template_name = 'blog/detail.html'
	context_object_name = 'artikel'

	def get_context_data(self,*args,**kwargs):
			kategori_list = self.model.objects.values_list('kategori',flat=True).distinct()
			self.kwargs.update({'kategori_list':kategori_list})
			artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
			self.kwargs.update({'artikel_serupa':artikel_serupa})
			kwargs = self.kwargs
			return super().get_context_data(*args,**kwargs)

class ArtikelListView(ListView):
	model = Artikel 
	template_name = 'blog/artikel_list.html'
	context_object_name = 'artikel_list'
	ordering = ['-published']
	paginate_by = 3

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori',flat=True).distinct()
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)


class ArtikelPerKategori():
	model = Artikel 

	def get_latest_artikel_each_kategori(self):
		kategori_list = self.model.objects.values_list('kategori',flat=True).distinct()
		queryset = []

		for kategori in kategori_list:
			artikel = self.model.objects.filter(kategori=kategori).latest('published')
			queryset.append(artikel)

		return queryset
class ArtikelKategoriListView(ListView):
	model = Artikel
	template_name = "blog/artikel_kategori_list.html"
	context_object_name = 'artikel_list'
	ordering = ['-published']
	paginate_by = 3

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
		return super().get_queryset()

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori',flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

