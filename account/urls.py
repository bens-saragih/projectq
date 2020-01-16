from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^login',views.LoginView.as_view(),name='login'),
	url(r'^logout',views.LogoutIndex.as_view(),name='logout'),
	url(r'^profile',views.View_Profile,name='view_profile'),
    url(r'^signup',views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^password_reset_index/',views.PasswordResetIndex.as_view(),name='password_reset_view'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_ \ -]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.PasswordConfirmResetIndex.as_view(),name='password_reset_confirm'),
    url(r'^password_reset_complete_view/',views.PasswordCompleteResetIndex.as_view(),name='password_reset_complete_view'),
    url(r'^password_reset_done_view/',views.PasswordResetDoneIndex.as_view(),name='password_reset_done_view'),
    url(r'^upload',views.UploadIndex.as_view(),name='upload'),
]


