from rest_framework import viewsets, generics, permissions
from .models import Event, Point
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, PointSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class EventAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class EventAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = IsOwnerOrReadOnly


class EventAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

