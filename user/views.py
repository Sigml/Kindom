from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator
from django.utils.http import urlsafe_base64_decode
# from .utils import send_email_verify, send_email_reset_password
from .forms import RegisterUserForm
from django.contrib.auth import login, logout
from django.views import View


class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        context = {
            'form':form
        }
        return render(request, 'registration.html', context)


class LoginUserView(View):
    pass


class LogoutUserView(View):
    pass