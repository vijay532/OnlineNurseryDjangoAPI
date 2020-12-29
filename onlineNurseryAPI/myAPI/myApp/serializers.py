from rest_framework import serializers

from .models import User,Nursery

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model=Nursery
        fields=('name','email')
