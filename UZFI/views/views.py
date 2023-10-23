from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from django.shortcuts import render
from News.models import *
from News.serializers import NewsContentSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Index(TemplateView):
    def get(self, request):
        try:
            faculty = Faculty.objects.all()
            serializers = FacultySerializer(faculty, many = True)
            direction  = Direction.objects.all()
            serializers1 = DirectionSerializer(direction, many = True)
            queryset = News_Content.objects.order_by('-date_created')[:10]
            serializer_class = NewsContentSerializer(queryset , many = True)
            return render(request, 'index.html',
                {"faculty":serializers.data,
                "direction":serializers1.data,
                "news":serializer_class.data
                })
        except Exception as e:
            return render(request, 'index.html')

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
        return render(request, 'councils-item.html',{"data":serializers.data})
    
class RequisitesApview(APIView):
    def get(self, request):
        requisites = Requisites.objects.last()
        serializers = RequisitesSerializer(requisites)
        return render(request, 'requesties.html',{"data":serializers.data})

class FinancialStatementsApview(APIView):
    def get(self, request):
        financialstatements = FinancialStatements.objects.all()
        serializers = FinancialStatementsSerializer(financialstatements, many = True)
        return render(request, 'financial-statements.html',{"data":serializers.data})

class VacanciesApview(APIView):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        serializers = VacanciesSerializer(vacancies, many = True)
        return render(request, '.html',{"data":serializers.data})

class OpenDataApview(APIView):
    def get(self, request):
        opendata = OpenData.objects.all()
        serializers = OpenDataSerializer(opendata, many = True)
        return render(request, 'open-data.html',{"data":serializers.data})

class FacultyApview(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializers = FacultySerializer(faculty, many = True)
        return render(request, 'faculties.html',{"data":serializers.data})
    
class FacultyByIdApview(APIView):
    def get(self, request, pk):
        faculty = Faculty.objects.get(id = pk)
        dekan = Dekan.objects.get(faculty = pk)
        serializers1 = GetDekanSerializer(dekan)
        serializers = FacultySerializer(faculty)
        return render(request, 'faculties-item.html',
            {"faculty":serializers.data,
             "dekan": serializers1.data
             })


class DirectionApview(APIView):
    def get(self, request, pk):
        direction = Direction.objects.get(id=pk)
        serializers = DirectionSerializer(direction)
        return render(request, 'destinations-item.html',{"data":serializers.data, })

class KafedraApview(APIView):
    def get(self, request):
        kafedra = Kafedra.objects.all()
        serializers = KafedraSerializer(kafedra, many = True)
        return render(request, 'departments.html',{"data":serializers.data})

class KafedraByIDApview(APIView):
    def get(self, request, pk):
        department = Kafedra.objects.filter(id = pk).last()
        serializers = KafedraSerializer(department)
        manager = KafedraManager.objects.get(kafedra = pk)
        serializers1 = KafedraManagerSerializer(manager)
        return render(request, 'departments-item.html',{
            "data":serializers.data,
            "manager" : serializers1.data
            })

class CentersDepartmentApiView(APIView):
    def get(self, request):
        centers_department = CentersDepartments.objects.all()
        serializers = CentersDepartmentsSerializer(centers_department, many = True)
        return render(request, 'centers.html', {"data":serializers.data})

class CentersDepartmentByIDApiView(APIView):
    def get(self, request, pk):
        center = CentersDepartments.objects.filter(id = pk).last()
        departmentmanager = CentersDepartmentsManager.objects.get(centers_departments = pk)
        serializers = CentersDepartmentsSerializer(center)
        serializers1 = CentersDepartmentsManagerSerializer(departmentmanager)
        return render(request, 'centers-item.html', {"data":serializers.data,
                                                "manager" : serializers1.data})
    
class CentersDepartmentManagerpiView(APIView):
    def get(self, request, pk):
        departments = CentersDepartmentsManager.objects.get(id = pk)
        serializers = CentersDepartmentsManagerSerializer(departments)
        return render(request, ".html", {"departments_manager":serializers.data})

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