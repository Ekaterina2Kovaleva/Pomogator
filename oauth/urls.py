from django.contrib import admin
from django.urls import path, include
from .endpoint import views, auth_views

urlpatterns = [
    path('', auth_views.google_login),
    path('google/', auth_views.google_auth)
]