from django.urls import path
from . import views

urlpatterns = [
    path("", views.aktuality, name="aktuality"),
    path("aktuality/new", views.post_new, name="post_new"),
    path("aktuality/<int:pk>/edit/", views.post_edit, name="post_edit"),
]
