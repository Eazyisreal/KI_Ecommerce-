from django.urls import path
from account import views


urlpatterns = [
    path('signup_user/', views.signup_user, name='signup_user'),
    path('authentication_login/', views.authentication_login, name='authentication_login'),
    path('authentication_reset_password/', views.authentication_reset_password, name='authentication_reset_password'),
    path('logout_user/', views.logout_user, name="logout_user"),


]
