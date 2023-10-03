from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class KafedraManagerApiview(APIView):
    def post(self, request):
        data = request.data
        kafedramanager = request.data['kafedramanager']
        role = User.objects.get(username=kafedramanager).role
        print(role)
        if role == 'KAFEDRAMANAGER':
            data['kafedramanager'] = User.objects.get(username=kafedramanager).id
            serializer = KafedraManagerSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Sizning role noto\'g\'ri'}, status=status.HTTP_400_BAD_REQUEST)