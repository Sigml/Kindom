from django.urls import path
from django.views.generic import TemplateView
from .views import (RegisterUserView, LoginUserView, LogoutUserView, EmailVerifyView, UserInfoView, ResetUserPasswordView, SearchUserToResetPasswordView,
                    UserUpdateInfoView, )


urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name = 'registration'),
    path('confirm_email/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerifyView.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='invalid_verify.html'), name='invalid_verify'),
    path('login/', LoginUserView.as_view(), name = 'login'),
    path('logout/', LogoutUserView.as_view(), name = 'logout'),
    path('reset_password/', SearchUserToResetPasswordView.as_view(), name='search_user_to_reset_password'),
    path('reset_password/<uid64>/<token>/', ResetUserPasswordView.as_view(), name='reset_password'),
    path('user_info/', UserInfoView.as_view(), name='user_info'),
    path('user_update/', UserUpdateInfoView.as_view(), name='user_update')
]
