from rest_framework import serializers
from .models import Event, Project
from rest_framework import serializers
from .models import Task, Link, Status, Type_Link


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tasks = TaskSerializer(source="task_set", many=True, read_only=True)
    links = LinkSerializer(source="link_set", many=True, read_only=True)
    class Meta:
        model = Event
        fields = '__all__'
        depth = 2


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = '__all__'
        depth = 2


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class Type_LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Link
        fields = '__all__'
