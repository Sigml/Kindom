from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator
from django.utils.http import urlsafe_base64_decode
from .utils import send_email_verification, send_email_reset_password
from django.contrib.auth import login, logout
from django.views import View
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseServerError
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import RegisterUserForm, LoginUserForm, SearchUserForm, ResetPasswordForm


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

                if is_token_valid:
                    user.email_verify = True
                    user.save()
                    login(request, user)
                    
                    return redirect('main')
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
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *agrs, **kwargs):
        form = self.form_class(request.POST)
        
        context = {
            'form':form
        }
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = CustomUser.objects.authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect (self.success_url)
            else:
                form.add_error(None, 'Nie prawidłowy email lub hasło')
                messages.error(request, 'Nie prawidłowy email lub hasło')
                
        return render(request, self.template_name, context)


class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')
    

class UserInfoView(View):
    def get(self, request, pk):
        return 


class SearchUserToResetPasswordView(View):
    form_class = SearchUserForm
    template_name = 'search_user.html'
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        context = {
            'form':form
        }     
        
        return render(request, self.template_name, context)
    
    def post(self, request, *agrs, **kwargs):
        form = self.form_class(request.POST)
        
        context = {
            'form':form
        }
        
        if form.is_valid():
            search_user = form.cleaned_data['username']      
            user =  CustomUser.objects.filter(Q(email=search_user) | Q(username=search_user)).first()
            
            if user:
                send_email_reset_password(request, user)
                return render(request, 'confirm_email.html')
            else:
                return HttpResponseServerError('Nie znaleziono użytkownika')
            
        return render(request, self.template_name, context)
                
    
class ResetUserPasswordView(View):
    form_class = ResetPasswordForm
    template_name = 'reset_password.html'
    success_url = '/'
    
    def get(self, request, uid64, token):
        user = self.get_user(uid64)
        form = self.form_class
        
        context = {
            'form':form
        }
        
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            
            return render(request, self.template_name, context)
        
    @staticmethod
    def get_user(uidb64):
        try:
            uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
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
    
    def post(self, request, uid64, token):
        user = self.get_user(uid64)
        form = self.form_class(request.POST)
        
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            
            if form.is_valid():
                cleaned_data = form.cleaned_data
                user.set_password(cleaned_data['password'])
                user.save()
                login(request, user)
                
                return redirect('main')
            
            else:
                return render(request, 'reset_password.html', {'form':form})
            
        else:
            return redirect ('invalid_verify')