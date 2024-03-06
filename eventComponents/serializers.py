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

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'

class Type_LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type_Link
        fields = '__all__'
