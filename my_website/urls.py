from django.conf.urls import url,include
from django.contrib import admin
from .views import index 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index.as_view(),name='index'),
    ###
    url(r'^artikel/',include('blog.urls',namespace='blog')),
    url(r'^account/',include('account.urls',namespace='account')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)