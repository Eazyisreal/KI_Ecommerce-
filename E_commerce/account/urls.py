from django.urls import path
from account import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('signup_user/', views.signup_user, name='signup_user'),
    path('authentication_login/', views.authentication_login, name='authentication_login'),
    path('authentication_reset_password/', views.authentication_reset_password, name='authentication_reset_password'),
    path('logout_user/', views.logout_user, name="logout_user"),

#     ### password Reset ###
#     path('reset_password/', auth_view.PasswordResetView.as_view(), name="reset_password"),
#     path('reset_password_send/', auth_view.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
