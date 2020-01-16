from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100,default='',null=True,blank=True)
	city = models.CharField(max_length=100,default='',null=True,blank=True)
	website = models.URLField(default='',null=True,blank=True)
	phone = models.IntegerField(default=62)
	image = models.ImageField(upload_to='profile_image',blank=True,null=True)

	title = models.TextField()
	
	def __str__(self):
		return "{}".format(self.user.username)	

	@property
	def get_photo_url(self):
	    if self.image and hasattr(self.image, 'url'):
	        return self.image.url
	    else:
	        return "/static/img/default.jpg"

            

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)