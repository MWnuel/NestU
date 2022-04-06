from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('details', views.details_view, name='details_view'),
    path("server/<int:server_id>", views.server_info, name = "server_info")
]
