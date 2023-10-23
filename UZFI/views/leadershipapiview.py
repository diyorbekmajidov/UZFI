from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from UZFI.models import *
from UZFI.serializers import *
from django.shortcuts import render

class LeadeshipAPIView(APIView):
    def get(self, request):
        try :
            leadership = Leadership.objects.all()
            serializers = LeadershipSerializer(leadership, many=True)
            return render(request, '.html',{"data":serializers.data})
        except Exception as e:
            return Response({"ok":[]})