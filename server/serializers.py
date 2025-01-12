from rest_framework import serializers
from .models import Channel, Server



class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    channel_server = ChannelSerializer(many=True, read_only=True)
    num_members = serializers.SerializerMethodField()
    
    class Meta:
        model = Server
        exclude = ('member', )
        
        fields = ["id", "name", "owner", "category", "description", "member", "channel_server"]

    def get_num_members(self,obj):
        if hasattr(obj,'num_members'):
            return obj.num_members
        return None