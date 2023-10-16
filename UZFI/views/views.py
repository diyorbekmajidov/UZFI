from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CharterApview(APIView):
    def get(self, request):
        charter = Charter.objects.all()
        serializers = CharterSerializer(charter, many = True) 
        return render(request, 'charter.html',{"data":serializers.data})
    

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

class DirectionListCreate(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionRetrieveUpdate(RetrieveUpdateDestroyAPIView):
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