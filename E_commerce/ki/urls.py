from django.urls import path
from ki import views
urlpatterns = [
    path('signup_user/', views.signup_user, name="signup_user")
]
