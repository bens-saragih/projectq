from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')   

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')





class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['city','website','description','phone']

class UploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

