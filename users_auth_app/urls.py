from django.urls import path
from users_auth_app import views

app_name = 'users_auth_app'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
]