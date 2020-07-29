from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.accounts_list, name="accounts_list"),
    path("register/", views.account_register, name="account_register"),
    path("account/<int:pk>/", views.account_details, name="account_details"),
    path("account/<int:pk>/update/", views.account_update, name="account_update"),
    path("account/<int:pk>/delete/", views.account_delete, name="account_delete"),
]
