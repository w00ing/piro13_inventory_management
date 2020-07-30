from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.products_list, name="products_list"),
    path("product/register/", views.product_register, name="product_register"),
    path("product/<int:pk>/", views.product_details, name="product_details"),
    path("product/<int:pk>/update/", views.product_update, name="product_update"),
    path("product/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("amount/", views.amount_ajax, name="amount_ajax"),
]
