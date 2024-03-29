from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="head"),
    path("choose", views.main_page, name="main_page"),
    path("graph1", views.index, name="graph1"),
    path("graph2", views.graph2, name="graph2"),
]