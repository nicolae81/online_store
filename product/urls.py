
from django.urls import path
from . import views
urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
    path('list_products/', views.ProductListView.as_view(), name='list-products'),
]
