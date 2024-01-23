from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("graph3", views.graph3, name="graph3"),
    path("graph4", views.graph4, name="graph4"),
    path("graph5", views.graph5, name="graph5")
]