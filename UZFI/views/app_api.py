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
import requests


class UzfiStatistika(APIView):
    def get(self, request):
        url_talabalr = 'https://student.uzfi.uz/rest/v1/public/stat-student'
        url_xodimlar = 'https://student.uzfi.uz/rest/v1/public/stat-employee'
        response_talabalar = requests.get(url_talabalr).json()
        response_employs = requests.get(url_xodimlar).json()
        
        respons = {
            "result" : [
                response_talabalar['data']['education_type'],
                response_talabalar['data']['level']['Bakalavr'][ "4-kurs"],
                response_employs['data']['position'],
            ]
        }
        return Response(respons)
    

class   RapidlyApps(APIView):
    def get(self, request):
        respons = {
            "stat": "Tezkor havolalar",
        }