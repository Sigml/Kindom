from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator
from django.utils.http import urlsafe_base64_decode
from .utils import send_email_verify, send_email_reset_password
from .forms import RegisterUserForm
from django.contrib.auth import login, logout
from django.views import View
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseServerError


class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        context = {
            'form':form
        }
        return render(request, 'registration.html', context)
    
    def post(self, request):
        try:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                password = data.pop('password_confirmation')
                
                user = CustomUser.objects.create_user(**data)
                user.set_password
                send_email_verify(request.user)
                return redirect
            else:
                context = {'form': form}
                return render(request, 'registration.html', context)
        except IntegrityError as e:
                return HttpResponseServerError('Użytkownik już istnieje')
        except Exception as e:
                message = "Coś poszło nie tak, spróbuj ponownie później"
                return render(request, 'registration.html', {'message': message})


class LoginUserView(View):
    def get(self, request):
        return render(request, 'login.html')


class LogoutUserView(View):
    pass