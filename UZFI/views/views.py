from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CharterListCreate(ListCreateAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer

class CharterRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Charter.objects.all()
    serializer_class = CharterSerializer

class DocumentCreate(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CouncilsListCreate(ListCreateAPIView):
    queryset = Councils.objects.all()
    serializer_class = CouncilsSerializer

class CouncilsRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Councils.objects.all()
    serializer_class = CouncilsSerializer

class RequisitesListCreate(ListCreateAPIView):
    queryset = Requisites.objects.all()
    serializer_class = RequisitesSerializer

class RequisitesRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Requisites.objects.all()
    serializer_class = RequisitesSerializer

class FinancialStatementsListCreate(ListCreateAPIView):
    queryset = FinancialStatements.objects.all()
    serializer_class = FinancialStatementsSerializer

class FinancialStatementsRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = FinancialStatements.objects.all()
    serializer_class = FinancialStatementsSerializer

class VacanciesListCreate(ListCreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer

class VacanciesRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer

class OpenDataListCreate(ListCreateAPIView):
    queryset = OpenData.objects.all()
    serializer_class = OpenDataSerializer

class OpenDataRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = OpenData.objects.all()
    serializer_class = OpenDataSerializer

class FacultyListCreate(ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyRetrieveUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer