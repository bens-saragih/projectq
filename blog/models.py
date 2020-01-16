from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

class Artikel(models.Model):
	judul 		= models.CharField(max_length=255)
	isi   		= models.TextField()
	kategori 	= models.CharField(max_length=255)
	dibuat 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	#is_published = models.NullBooleanField(default=False)
	published = models.DateTimeField(null=True)
	slug 		= models.SlugField(blank=True,editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):# sehinggan saat selesai create di akan menggunakan dan menggambil absolute dan menampalikan di detail
		url_slug = {'slug':self.slug}
		return reverse('blog:detail',kwargs = url_slug)
		# reverse == mengembalikan
		# get_absolute_url tujuan setelah createview di buat, dan reverse mengembalikan ke detail yang dimana url nya ada slug

	def __str__(self):
		return "{}.{}".format(self.id,self.judul)
"""	class Meta:
		default_permissions = ('add','change','delete')# membuat hanya add saja,lakuan sebelum migrate, alternatifnya jika sudah di migrate lakukan unmakemigrations akan kembali awal
		permissions = (
			('publish_artikel','Can publish artikel'),# untuk custom gunakan permission
			)"""


"""
	def save(self):
		if self.is_published == True:
			self.published = timezone.now()

		else:
			self.published = None 
		super().save()"""

