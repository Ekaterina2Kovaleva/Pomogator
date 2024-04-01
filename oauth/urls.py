from django.contrib import admin
from django.urls import path, include
from .endpoint import views, auth_views

urlpatterns = [
    path('', auth_views.google_login),
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('google/', auth_views.google_auth)
]