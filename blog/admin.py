from django.contrib import admin

# Register your models here.
from .models import Artikel


# berguna untuk hanya bisa di baca saja
class ArtikelAdmin(admin.ModelAdmin):
	readonly_fields=[
						'slug',
						'updated',
						'dibuat',
						'published'
						
					]


"""class ArtikelAdmin(admin.ModelAdmin):
	def get_readonly_fields(self,request,obj):
		current_user = request.user 
		if obj != None:
			if current_user.has_perm("blog.publish_artikel"):
				readonly_fields = [
					'dibuat',
					'updated',
					'published',
					'slug'
				]
				return readonly_fields
			elif current_user.has_perm("blog.add_artikel"):
				if obj.is_published:
					return [data.name for data in self.model._meta.fields]
				else:
					readonly_fields = [
						'dibuat','updated','is_published','published','slug'
					]
					return readonly_fields
		else:
			readonly_fields = [
				'dibuat','updated','is_published','published','slug'
			]
			return readonly_fields"""

admin.site.register(Artikel, ArtikelAdmin)