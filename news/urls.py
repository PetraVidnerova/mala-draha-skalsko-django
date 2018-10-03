from django.urls import path
from . import views

urlpatterns = [
    path("", views.aktuality, name="aktuality"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("<int:pk>/detail/", views.post_detail, name="post_detail"),
]
