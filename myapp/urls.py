from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("hello/<str:parametro>", views.hi),
    path("projects/", views.projects),
    path("tasks/<int:id>", views.tasks),
]