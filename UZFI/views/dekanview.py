from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import Dekan
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class AllDekan(ListCreateAPIView):
    queryset = Dekan.objects.all()
    serializer_class = GetDekanSerializer

class GetDekanById(APIView):
    def get(self, request, pk):
        try:
            data = Dekan.objects.get(id=pk)
            serializers = GetDekanSerializer(data)
            return Response(serializers.data)
        except:
            return Response({"403":"user topilmadi"})

    
class DekanGetApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        serializers = GetDekanSerializer(dekan)
        return Response(serializers.data)
    
    def put(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        serializer = DekanSerializer(dekan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        dekan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    