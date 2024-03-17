from django import forms
from .models import CustomUser


class RegisterUserForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Powtórz hasło'
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name', 'date_of_birth',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nickname'
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'password'
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Imię'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nazwiśko'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class':'form-control',
                'placeholder':'Data urodzenia'
            })
        }