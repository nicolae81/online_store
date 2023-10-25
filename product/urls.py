
from django.urls import path
from . import views
urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
    path('list_products/', views.ProductListView.as_view(), name='list-products'),
    path('update_product/<int:pk>', views.ProductUpdateView.as_view(), name='update-product'),
    path('delete_product/<int:pk>', views.ProductDeleteView.as_view(), name='delete-product'),
    path('details_product/<int:pk>', views.ProductDetailView.as_view(), name='details-product'),
    path('delete_modal_product/<int:pk>/', views.delete_product_modal, name='delete-modal-product'),
]
