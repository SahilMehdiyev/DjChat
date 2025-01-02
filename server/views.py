from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer




class ServerListAPIView(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset