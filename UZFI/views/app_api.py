from rest_framework.views import APIView
from rest_framework.response import Response
from UZFI.models import *
from UZFI.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import requests


class UzfiStatistika(APIView):
    @swagger_auto_schema(
        operation_description="Bu view uchun Swagger dokumentatsiyasi",
        responses={200: openapi.Response('List of news content')}
    )
    def get(self, request):
        url_talabalr = 'https://student.uzfi.uz/rest/v1/public/stat-student'
        url_xodimlar = 'https://student.uzfi.uz/rest/v1/public/stat-employee'
        response_talabalar = requests.get(url_talabalr).json()
        response_employs = requests.get(url_xodimlar).json()

    
        result_ru = [
            {
                "Холостяк": {
                    "Мужской": 2840,
                    "Женщина": 7667
                },
                "Владелец": {
                    "Мужской": 68,
                    "Женщина": 146
                }
            },
            {
                "Дневное время": 1140,
                "Внешне": 1492,
                "Вечер": 281,
            },
            {
                "Стажер-преподаватель": 10,
                "Ассистент": 288,
                "Kучитель-атта": 27,
                "Доцент": 46,
                "Профессор": 6,
                "Руководитель отдела": 20
            }
        ]
        
        result_en =  [
            {
                "Bachelor": {
                    "Male": 2840,
                    "Female": 7667
                },
                "Magistr": {
                    "Male": 68,
                    "Female": 146
                }
            },
            {
                "Daytime": 1140,
                "Externally": 1492,
                "Evening": 281,
            },
            {
                "Intern-teacher": 10,
                "Assistant": 288,
                "Head teacher": 27,
                "Docent": 46,
                "Professor": 6,
                "Head of the department": 20
            }
        ]  
        
        respons = {
            "respons_ru":result_ru,
            "respons_en" : result_en,
            "respons_uz" : [
                response_talabalar['data']['education_type'],
                response_talabalar['data']['level']['Bakalavr'][ "4-kurs"],
                response_employs['data']['position'],
            ]
        }
        return Response(respons)
    

class   RapidlyApps(APIView):
    @swagger_auto_schema(
        operation_description="Bu view uchun Swagger dokumentatsiyasi",
        responses={200: openapi.Response('List of news content')}
    )
    def get(self, request):
        respons = {
            "status": "Tezkor havolalar",
            "result" : [
            {
                "title": "Uzfi yagona interaktiv xizmatlar portali",
                "link": "https://interactive.uzfi.uz/",
                "icon": "https://uzfi.uz/static/assets/images/Frame_1975515.png",
            },
            {
                "title": "Elektron kutubxona",
                "link": "https://library.uzfi.uz/#",
                "icon": "https://uzfi.uz/static/assets/images/hovered_NMw9C2X.png",
            },
            {
                "title": "Dars jadvali",
                "link": "https://darsjadvali.uzfi.uz/",
                "icon": "https://uzfi.uz/static/assets/images/Frame_197552_cLFs5Ov.png",
            },
            {
                "title": "Korporativ elektron pochta",
                "link": "https://biz.mail.ru/login/uzfi.uz",
                "icon": "https://uzfi.uz/static/assets/images/Frame_197551_67eivVm.png",
            },
            {
                "title": "Kpi tizimi",
                "link": "https://kpi.uzfi.uz/",
                "icon": "https://uzfi.uz/static/assets/images/hovered_NMw9C2X.png",
            },
            {
                "title": "TTJ",
                "link": "https://ttj.uzfi.uz/",
                "icon": "https://uzfi.uz/static/assets/images/hovered_NMw9C2X.png"
            }
            ]
        }
        return Response(respons)