from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class KafedraManagerApview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        kafedramanager = KafedraManager.objects.get(kafedramanager=request.user)     
        serializers   = GetKafedraManagerSerializer(kafedramanager)
        return Response(serializers.data)
    
    def put(self, request):
        kafedramanager = KafedraManager.objects.get(kafedramanager=request.user)
        serializers =  KafedraManagerSerializer(kafedramanager, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def delete(self, request):
        kafedramanager = KafedraManager.objects.get(kafedramanager=request.user)
        kafedramanager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetAllKafedraManager(ListCreateAPIView):
    queryset = KafedraManager.objects.all()
    serializer_class = GetKafedraManagerSerializer

