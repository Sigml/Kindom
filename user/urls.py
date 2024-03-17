from django.urls import path
from django.views.generic import TemplateView
from .views import RegisterUserView, LoginUserView, LogoutUserView, EmailVerifyView, UserInfoView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('confirm_email/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerifyView.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='invalid_verify.html'), name='invalid_verify'),
    path('login/', LoginUserView.as_view(), name = 'login'),
    path('logout/', LogoutUserView.as_view(), name = 'logout'),
    path('user_info', UserInfoView.as_view(), name='user_info'),
]
