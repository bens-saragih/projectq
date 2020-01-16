from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User 
from django.views.generic import TemplateView
from django.views.generic import TemplateView,DetailView,CreateView,ListView
## confirmation email ##
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,UploadForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LogoutView,

    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .forms import UserUpdateForm,UserEdit

class LogoutIndex(LoginRequiredMixin,LogoutView):
	template_name = 'account/logout.html'


class LoginIndex(LoginView):
    template_name = 'account/login.html'

class PasswordResetIndex(PasswordResetView):
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('account:password_reset_done_view')
    email_template_name = 'account/password_reset_email.html' 

class PasswordResetDoneIndex(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class PasswordConfirmResetIndex(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete_view')

class PasswordCompleteResetIndex(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'

class LoginView(LoginView,FormMixin):
	template_name = 'login.html'


 

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Silakan konfirmasi akun kamu dengan link yang sudah kami kirim ke Mail ')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Selamat akun kamu sudah aktif dan sudah bisa digunakan ')
    else:
        return HttpResponse('Link tidak valid atau sudah pernah dibuka')

@login_required
def View_Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UploadForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        e_form = UserEdit(request.POST,instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid() and e_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Perubahan telah tersimpan')
            return redirect('account:view_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UploadForm(instance=request.user.userprofile)
        e_form = UserEdit(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'e_form': e_form,
        'user':request.user
    }


    return render(request, 'view_profile.html', context)


class UploadIndex(CreateView):
    model = UserProfile
    form_class = UploadForm
    success_url = reverse_lazy('account:view_profile')
    template_name = 'account/upload.html'

