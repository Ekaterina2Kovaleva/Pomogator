"""
URL configuration for Pomogator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from event.views import (EventAPIList, EventAPIUpdate, EventAPIDestroy, ProjectAPIUpdate, ProjectAPIList,
                         ProjectAPIDestroy, LinkAPIList, LinkAPIUpdate, LinkAPIDestroy, TaskAPIList, TaskAPIUpdate,
                         TaskAPIDestroy, StatusViewSet, Type_LinkViewSet)
from google_docs.views import FileCreateAPIView
from oauth.endpoint.views import RoleViewSet

router = routers.SimpleRouter()
router.register(r'type_link', Type_LinkViewSet)
router.register(r'status', StatusViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),#http://127.0.0.1:8000/api/v1/event/
    path('api/v1/event/', EventAPIList.as_view()),
    path('api/v1/event/<int:pk>/', EventAPIUpdate.as_view()),
    path('api/v1/eventdelete/<int:pk>/', EventAPIDestroy.as_view()),
    path('api/v1/project/', ProjectAPIList.as_view()),
    path('api/v1/project/<int:pk>/', ProjectAPIUpdate.as_view()),
    path('api/v1/projectdelete/<int:pk>/', ProjectAPIDestroy.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/linkdelete/<int:pk>/', LinkAPIDestroy.as_view()),
    path('api/v1/link/', LinkAPIList.as_view()),
    path('api/v1/link/<int:pk>/', LinkAPIUpdate.as_view()),
    path('files/', FileCreateAPIView.as_view(), name="file-create"),
    path('api/v1/', include('oauth.urls')),
]