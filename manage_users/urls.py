from django.urls import path
from manage_users import views

urlpatterns = [
    path('create_user/', views.UserCreateView.as_view(), name='create-user'),
    ]
