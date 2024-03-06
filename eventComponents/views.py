from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Task, Type_Link, Status, Link
from .serializers import TaskSerializer, Type_LinkSerializer, StatusSerializer, LinkSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class Type_LinkViewSet(viewsets.ModelViewSet):
    queryset = Type_Link.objects.all()
    serializer_class = Type_LinkSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Type_Link.objects.all()
    serializer_class = StatusSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class LinkAPIList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = IsAuthenticatedOrReadOnly



class LinkAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class LinkAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = IsAuthenticatedOrReadOnly