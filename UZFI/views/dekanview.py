from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DekanApiview(APIView):
    def post(self, request):
        data = request.data
        serializer = DekanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
class DekanGetApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        print(dekan.faculty)
        serializers = DekanSerializer(dekan)
        return Response(serializers.data)