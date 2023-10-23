from category import views
from django.urls import path

urlpatterns = [
    path('create_category', views.CategoryCreateView.as_view(), name='create-category'),
    path('list_categories', views.CategoryListView.as_view(), name='list-categories'),
]