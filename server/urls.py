
from django.urls import path

from server.views import ServerListAPIView


urlpatterns = [
    path('servers/', ServerListAPIView.as_view(), name='server-list'),
]
