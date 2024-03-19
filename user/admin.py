from django.contrib import admin
from .models import CustomUser



class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password',
        'profile_picture', 'email_verify','verification_token'
    )
    search_fields = (
        'username', 'first_name', 'last_name', 'email', 'number_phone', 'password', 'email_verify','verification_token'
    )


admin.site.register(CustomUser, CustomUserAdmin)