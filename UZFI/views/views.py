from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView
from News.models import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CharterApview(TemplateView):
    def get(self, request):
        charter = Charter.objects.all()
        serializers = CharterSerializer(charter, many = True) 
        return render(request, 'charter.html',{"data":serializers.data})

class DocumentCreateApview(APIView):
    def get(self,request):
        document = Document.objects.all()
        serializers = DocumentSerializer(document, many = True)
        return render(request, 'documents.html',{"data":serializers.data})

class CouncilsApview(APIView):
    def get(self, request):
        councils = Councils.objects.all()
        serializers = CouncilsSerializer(councils, many = True)
        return render(request, 'councils.html',{"data":serializers.data})
    
class CouncilsByIdApview(APIView):
    def get(self, request, pk):
        councils = Councils.objects.get(id = pk)
        serializers = CouncilsSerializer(councils)
        return render(request, '.html',{"data":serializers.data})
    
class RequisitesApview(APIView):
    def get(self, request):
        requisites = Requisites.objects.last()
        serializers = RequisitesSerializer(requisites)
        return render(request, '.html',{"data":serializers.data})

class FinancialStatementsApview(APIView):
    def get(self, request):
        financialstatements = FinancialStatements.objects.all()
        serializers = FinancialStatementsSerializer(financialstatements, many = True)
        return render(request, '.html',{"data":serializers.data})

class VacanciesApview(APIView):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        serializers = VacanciesSerializer(vacancies, many = True)
        return render(request, '.html',{"data":serializers.data})

class OpenDataApview(APIView):
    def get(self, request):
        opendata = OpenData.objects.all()
        serializers = OpenDataSerializer(opendata, many = True)
        return render(request, '.html',{"data":serializers.data})

class FacultyApview(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializers = FacultySerializer(faculty, many = True)
        return render(request, '.html',{"data":serializers.data})

class DirectionListCreate(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class KafedraListCreate(ListCreateAPIView):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer    


class ScientificWorkAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = ScientificWorkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = ScientificWork.objects.filter(user=request.user)
        serializers = ScientificWorkSerializer(data, many = True)
        return Response(serializers.data)