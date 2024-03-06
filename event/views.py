from rest_framework import viewsets, generics, permissions
from .models import Event
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EventAPIList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class EventAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



class EventAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

