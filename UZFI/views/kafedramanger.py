from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models import *
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class KafedraManagerGet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        kafedramanager = KafedraManager.objects.get(kafedramanager=request.user)
        serializers   = GetKafedraManagerSerializer(kafedramanager)
        return Response(serializers.data)
    