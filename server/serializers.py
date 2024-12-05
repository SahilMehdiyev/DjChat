from rest_framework import serializers
from .models import Server,Category


class ServerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Server
        fields = [
                'id',
                'name',
                'owner',
                'category',
                'description',
                'member'
            ]