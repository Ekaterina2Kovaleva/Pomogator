from rest_framework import serializers

from oauth.models import AuthUser, Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


class GoogleAuth(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
