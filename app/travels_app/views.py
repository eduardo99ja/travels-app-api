from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Travel
from travels_app.serializers import TravelSerializer


class TravelList(generics.ListAPIView):
    """List all travels"""
    serializer_class = TravelSerializer
    queryset = Travel.objects.all()


class TravelCreateAV(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        user = self.request.user
        if serializer.is_valid():
            serializer.save(user=user)
            data = {"data": serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
