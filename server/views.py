from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Server
from .serializers import ServerSerializer


class ServerListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_serverid = request.query_params.get("by_serverid")

        queryset = Server.objects.all()

        if by_serverid:
            try:
                if not by_serverid.isdigit():
                    raise ValidationError(
                        detail=f"Invalid server id '{by_serverid}'. Must be numeric."
                    )
                queryset = queryset.filter(id=int(by_serverid))
                if not queryset.exists():
                    return Response([], status=404)
            except ValueError:
                return Response([], status=404)

        if category:
            queryset = queryset.filter(category__name=category)

        if by_user:
            queryset = queryset.filter(member__id=request.user.id)

        if qty:
            try:
                qty = int(qty)
                queryset = queryset[:qty]
            except ValueError:
                raise ValidationError(detail=f"Invalid quantity value: {qty}")

        serializer = ServerSerializer(queryset, many=True)
        return Response(serializer.data)
