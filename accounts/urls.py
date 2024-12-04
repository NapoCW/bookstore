from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('already_logged_in/', views.already_logged_in_view, name='already_logged_in'),
    path('logout/', views.logout_view, name='logout'),
]