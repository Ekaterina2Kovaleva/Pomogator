from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Profile
        fields = '__all__'
