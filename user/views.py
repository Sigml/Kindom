from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator
from django.utils.http import urlsafe_base64_decode
from .utils import send_email_verification, send_email_reset_password
from .forms import RegisterUserForm
from django.contrib.auth import login, logout
from django.views import View
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from django.urls import reverse_lazy


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
                user.set_password(password)
                send_email_verification(request, user)
                return redirect('confirm_email')
            else:
                context = {'form': form}
                return render(request, 'registration.html', context)
        except IntegrityError as e:
                return HttpResponseServerError('Użytkownik już istnieje')
        except Exception as e:
                print(e)
                message = "Coś poszło nie tak, spróbuj ponownie później"
                return render(request, 'registration.html', {'message': message})
            

class EmailVerifyView(View):
    def get(self, request, uidb64, token):
        try:
            user = self.get_user(uidb64)
            print(f"User: {user}, Token: {token}")

            if user is not None:
                is_token_valid = token_generator.check_token(user, token)
                print(f"Is token valid: {is_token_valid}")

                if is_token_valid:
                    user.email_verify = True
                    user.save()
                    login(request, user)
                    
                    print(f"email_verify status after saving: {user.email_verify}")
                    
                    return redirect('login')
        except Exception as e:
            print(f"Błąd weryfikacji emaila: {e}")
            return HttpResponseServerError("Wystąpił błąd podczas weryfikacji emaila.")
        
        return redirect('invalid_verify')


    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            CustomUser.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user



class LoginUserView(View):
    def get(self, request):
        return render(request, 'login.html')


class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')

class UserInfoView(View):
    pass