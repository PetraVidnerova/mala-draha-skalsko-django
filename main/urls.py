from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("onas", views.onas, name="onas"),
    path("fotky", views.fotky, name="fotky"),
    path("planek", views.planek, name="planek"),
    path("odkazy", views.odkazy, name="odkazy"),
    path("edit", views.edit, name="edit"),
]
