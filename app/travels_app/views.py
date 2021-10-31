from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from travels_app.serializers import CategorySerializer

from core.models import Travel, Category
from travels_app.serializers import TravelSerializer, TravelCategorySerializer


class TravelList(generics.ListAPIView):
    """List all travels"""
    serializer_class = TravelCategorySerializer
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
                            status=status.HTTP_400_BAD_REQUEST)


class CategoryList(generics.ListAPIView):
    """List all categories"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CategoryCreateAV(generics.CreateAPIView):
    """Create new category object"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"success": "ok", "data": serializer.data}
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
