from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from UZFI.models.models import *
from UZFI.serializers import *
from django.shortcuts import render
from News.models import *
import requests
from News.serializers import NewsContentSerializer, PopularStudentsSerializer


class Index(TemplateView):
    def get(self, request):
        try:
            faculty = Faculty.objects.all()
            serializers = FacultySerializer(faculty, many = True)
            direction  = Direction.objects.filter(direction_type='bakalavir')
            serializers1 = DirectionSerializer(direction, many = True)
            queryset = News_Content.objects.order_by("-date_created")[:5]
            serializer_class = NewsContentSerializer(queryset , many = True)
            popular_student  = PopularStudents.objects.order_by("date_created")[:5]
            serializer_popular_students = PopularStudentsSerializer(popular_student, many=True)
            

            charter = Charter.objects.order_by("-date_created")[:5] # unversity nizomi
            charter_serializers = CharterSerializer(charter, many = True) 

            mainpage_category = NewsCategory.objects.get(new_category="MAINPAGE")

            url_talabalr = 'https://student.uzfi.uz/rest/v1/public/stat-student'
            url_structure = 'https://student.uzfi.uz/rest/v1/public/stat-structure'
            url_xodimlar = 'https://student.uzfi.uz/rest/v1/public/stat-employee'

            try:
                response_talabalar = requests.get(url_talabalr).json()
                response_structure = requests.get(url_structure).json()
                response_xodimlar = requests.get(url_xodimlar).json()
                indicators = {
                    "response_talabalar": response_talabalar["data"]["education_type"]["Jami"],
                    "response_structure": response_structure["data"]["departments"],
                    "response_structure1": response_structure["data"]["auditoriums"],
                    "response_xodimlar": response_xodimlar["data"]["employment_form"],
                    "response_uqtuvchilar": response_xodimlar["data"]["position"],
                    "all_students_count": response_talabalar["data"]["education_type"]["Jami"]['Erkak'] + response_talabalar["data"]["education_type"]["Jami"]['Ayol']
                }
            except Exception as e:
                indicators = {
                    "response_talabalar": {
                        "Erkak":0,
                        "Ayol":0},
                    "response_structure": [
                        {'count':0},
                        {'count':0},
                        {'count':0},
                        {'count':0},
                        {'count':0},
                        {'count':0},
                    ],
                    "response_structure1": [
                        {'count':0},
                        {'count':0},
                        {'count':0},
                        {'count':0},
                        {'count':0},
                    ],
                    "response_xodimlar": {
                        "Asosiy ish joy": 0,
                    },
                    "response_uqtuvchilar": {
                        "Dotsent":0,
                        "Professor":0,
                        "Katta o‘qituvchi":0
                    },
                    "all_students_count": '000'}
            
            context = {"faculty":serializers.data, 
                       "direction":serializers1.data,
                        "news":serializer_class.data, 
                        "popular_student":serializer_popular_students.data, 
                        "indicators" : indicators,
                        "charter":charter_serializers.data,
                        }
            if mainpage_category:
                mainpage_news = News_Content.objects.filter(category=mainpage_category)
                serializers_context = NewsContentSerializer(mainpage_news.last())
                context['MAINPAGE'] = serializers_context.data

        

            return render(request, 'index.html', context=context)
        except Exception as e:
            print(e)
            return render(request, 'index.html')


def green_institute(request):
    try:
        green_institute = GreenInstitute.objects.first()

        category = News_Content.objects.filter(category=1).order_by("-date_created")  # So‘ngi yangiliklar birinchi chiqadi
        serializer = NewsContentSerializer(category, many=True)
        page = Paginator(category, 6)
        page_num = int(request.GET.get('page', 1))

        return render(request, 'green-institute.html', {
            "page_obj": page.page(page_num),
            "category": serializer.data,  
            "green_institute": green_institute  
        })
    except Exception as e:
        print(f"Error retrieving news content: {e}")
        return render(request, 'green-institute.html')



class Charterview(TemplateView):
    def get(self, request):
        try:
            charter = Charter.objects.all()
            serializers = CharterSerializer(charter, many = True) 
            return render(request, 'charter.html',{"data":serializers.data})
        except:
            return render(request,'charter.html')

class DocumentCreateview(TemplateView):
    def get(self,request):
        try:
            document = Document.objects.all()
            serializers = DocumentSerializer(document, many = True)
            return render(request, 'documents.html',{"data":serializers.data})
        except:
            return render(request,'documents.html')
        
class DocumentCreateApiview(APIView):
    def get(self, request):
        try:
            document = Document.objects.all()
            serializers = DocumentSerializer(document, many = True)
            return Response({"data": serializers.data})
        except:
            return Response({403:"Malumot topilmadi."})

class Councilsview(TemplateView):
    def get(self, request, pk = None):
        if pk is None:
            councils = Councils.objects.all().order_by('id')
            serializers = CouncilsSerializer(councils, many = True)
            return render(request, 'councils.html',{"data":serializers.data})
        
        councils = Councils.objects.get(id = pk)
        councils_manager = CentersDepartmentsManager.objects.get(councils = pk)
        serializers_councils = CentersDepartmentsManagerSerializer(councils_manager)
        serializers = CouncilsSerializer(councils)
        return render(request, 'councils-item.html',{"data":serializers.data, "manager":serializers_councils.data})
    
class CouncilsApiview(APIView):
    def get(self, request, pk = None):
        if pk is None:
            councils = Councils.objects.all().order_by('number')
            serializers = CouncilsSerializer(councils, many = True)
            return Response({"data":serializers.data})
        
        councils = Councils.objects.get(id = pk)
        councils_manager = CentersDepartmentsManager.objects.get(councils = pk)
        serializers_councils = CentersDepartmentsManagerSerializer(councils_manager)
        serializers = CouncilsSerializer(councils)
        return Response({"data":serializers.data,"manager":serializers_councils.data})
    
class Requisitesview(TemplateView):
    def get(self, request):
        requisites = Requisites.objects.last()
        serializers = RequisitesSerializer(requisites)
        return render(request, 'requesties.html',{"data":serializers.data})
    
class RequisitesApiview(APIView):
    def get(self, request):
        requisites = Requisites.objects.last()
        serializers = RequisitesSerializer(requisites)
        return Response({"data":serializers.data})





class OpenDataview(TemplateView):
    def get(self, request):
        opendata = OpenData.objects.all()
        serializers = OpenDataSerializer(opendata, many = True)
        return render(request, 'open-data.html',{"data":serializers.data})
    
class OpenDataApiview(APIView):
    def get(self, request):
        opendata = OpenData.objects.all()
        serializers = OpenDataSerializer(opendata, many = True)
        return Response({"data":serializers.data})

class Facultyview(TemplateView):
    def get(self, request, pk=None):
        if pk is None:
            faculty = Faculty.objects.all()
            serializers = FacultySerializer(faculty, many = True)
            return render(request, 'faculties.html',{"data":serializers.data})
        
        try:
            faculty = Faculty.objects.get(id = pk)
            dekan = Dekan.objects.get(faculty = pk)
            directions = Direction.objects.filter(faculty=pk)
            kafedra = Kafedra.objects.filter(faculty=pk)
            serializers_kafedra = KafedraSerializer1(kafedra, many = True)
            serializers_directions = DirectionSerializer(directions, many = True)
            serializers1 = GetDekanSerializer(dekan)
            serializers = FacultySerializer(faculty)
            return render(request, 'faculties-item.html',
                {"faculty":serializers.data,
                "dekan": serializers1.data,
                "direction": serializers_directions.data,
                "kafedra": serializers_kafedra.data
                })
        except Exception as e:
            print(e)
            return render(request,'faculties-item.html')

class FacultyApiview(APIView):
    def get(self, request, pk=None):
        if pk is None:
            faculty = Faculty.objects.all()
            serializers = FacultySerializer(faculty, many = True)
            return Response({"data":serializers.data})
        
        try:
            faculty = Faculty.objects.get(id = pk)
            dekan = Dekan.objects.get(faculty = pk)
            directions = Direction.objects.filter(faculty=pk)
            kafedra = Kafedra.objects.filter(faculty=pk)
            serializers_kafedra = KafedraSerializer1(kafedra, many = True)
            serializers_directions = DirectionSerializer(directions, many = True)
            serializers1 = GetDekanSerializer(dekan)
            serializers = FacultySerializer(faculty)
            return Response(
                {"faculty":serializers.data,
                "dekan": serializers1.data,
                "direction": serializers_directions.data,
                "kafedra": serializers_kafedra.data
                })
        except Exception as e:
            print(e)
            return Response({403:"malo'mot topilmadi."})

class DekanById(TemplateView):
    def get(self, request, pk):
        try:
            dekan = Dekan.objects.get(id=pk)
            serializer = GetDekanSerializer(dekan)
            context = {"dekan":serializer.data,}
            return render(request, "dekan.html", context=context)
        except:
            return render(request,'dekan.html')
        
class DekanByIdApi(APIView):
    def get(self, request, pk):
        try:
            dekan = Dekan.objects.get(id=pk)
            serializer = GetDekanSerializer(dekan)
            user = dekan.dekan.id
            return Response({"dekan":serializer.data})
        except:
            return Response({403:"ma'lumot topilmadi"})

class Directionview(TemplateView):
    def get(self, request, pk):
        try :
            direction = Direction.objects.get(id=pk)
            serializers = DirectionSerializer(direction)
            return render(request, 'destinations-item.html',{"data":serializers.data, })
        except Exception as e:
            print(e)
            return render(request, 'destinations-item.html')
        
class DirectionApiview(APIView):
    def get(self, request, pk):
        try :
            direction = Direction.objects.get(id=pk)
            serializers = DirectionSerializer(direction)
            return Response({"data":serializers.data})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})
        
class DirectionMagistrview(TemplateView):
    def  get(self, request):
        try:
            direction_magistr = Direction.objects.filter(direction_type='magistratura')
            serializers = DirectionSerializer(direction_magistr,many=True)
            return render(request, 'magistr/mag.html',{
                "data":serializers.data
                })
        except Exception as e:
            print(e)

class DirectionMagistrApiview(APIView):
    def  get(self, request):
        try:
            direction_magistr = Direction.objects.filter(direction_type='magistratura')
            serializers = DirectionSerializer(direction_magistr,many=True)
            return Response({"data":serializers.data})
        except Exception as e:
            print(e)
class Kafedraview(TemplateView):
    def get(self, request, pk=None):
        if pk is None:
            kafedra = Kafedra.objects.all()
            serializers = KafedraSerializer(kafedra, many = True)
            return render(request, 'departments.html',{"data":serializers.data})

        try:
            department = Kafedra.objects.get(id = pk)
            print(department,'salom')
            serializers = KafedraSerializer(department)
            manager = KafedraManager.objects.filter(kafedra = pk).last()
            serializers1 = KafedraManagerSerializer(manager)
            return render(request, 'departments-item.html',{
                "data":serializers.data,
                "manager" : serializers1.data
                })
        except Exception as e:
            print(e)
            return render(request, 'departments-item.html')
    
class KafedraApiview(APIView):
    def get(self, request, pk=None):
        if pk is None:
            kafedra = Kafedra.objects.all()
            serializers = KafedraSerializer(kafedra, many = True)
            return Response({"kafedra":serializers.data})

        try:
            department = Kafedra.objects.get(id = pk)
            serializers = KafedraSerializer(department)
            manager = KafedraManager.objects.filter(kafedra = pk).last()
            serializers1 = KafedraManagerSerializer(manager)
            return Response({
                "kafedra": serializers.data,
                "manager": serializers1.data
                })
        except Exception as e:
            print(e)
            return Response({403:"ma'lumot topilmadi"})

class KafedraManagerById(TemplateView):
    def get(self, request, pk):

        manager = KafedraManager.objects.get(id = pk)
        serializer = KafedraManagerSerializer(manager)
        context = {"kafedra_manager":serializer.data,}

        return render(request, "department-manager.html", context=context)
    
class KafedraManagerByIdApi(APIView):
    def get(self, request, pk):
        manager = KafedraManager.objects.get(id = pk)
        serializer = KafedraManagerSerializer(manager)
        return Response({"kafedra_manager":serializer.data,})

class CentersDepartmentView(TemplateView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                center = CentersDepartments.objects.filter(id = pk).last()
                departmentmanager = CentersDepartmentsManager.objects.get(centers_departments = pk)
                serializers = CentersDepartmentsSerializer(center)
                serializers1 = CentersDepartmentsManagerSerializer(departmentmanager)
                return render(request, 'centers-item.html', {"data":serializers.data,
                                                        "manager" : serializers1.data})
            except:
                return render(request, 'centers-item.html')
        try:
            centers_department = CentersDepartments.objects.filter(role = "MARKAZ").order_by('number')
            serializers = CentersDepartmentsSerializer(centers_department, many = True)
            return render(request, 'centers.html', {"data":serializers.data})
        except Exception as e:
            print(e)
            return render(request, 'centers.html')
        
class DepartmentsView(TemplateView):
    def get(self, request):
        try:
            centers_department = CentersDepartments.objects.filter(role = "BO'LIM").order_by('number')
            serializers = CentersDepartmentsSerializer(centers_department, many = True)
            return render(request, 'bulimlar.html', {"data":serializers.data})
        except Exception as e:
            print(e)
            return render(request, 'bulimlar.html')
        
class CentersDepartmentApiView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                center = CentersDepartments.objects.get(id = pk)
                departmentmanager = CentersDepartmentsManager.objects.get(centers_departments = pk)
                serializers = CentersDepartmentsSerializer(center)
                serializers1 = CentersDepartmentsManagerSerializer(departmentmanager)
                return Response({"center-department":serializers.data,"manager" : serializers1.data})
            except:
                return Response({403:"ma'lumot topilmadi"})
        try:
            centers_department = CentersDepartments.objects.filter(role = "MARKAZ").order_by('number')
            serializers = CentersDepartmentsSerializer(centers_department, many = True)
            return Response({"centers_department":serializers.data})
        except Exception as e:
            return Response({403:"ma'lumot topilmadi"})
    
class TutorView(TemplateView):
    def get(self, request, pk=None):
        if pk is None:
            try:
                turor = Tutor.objects.all()
                page = Paginator(turor, 9)
                faculty = Faculty.objects.all()
                serializer = FacultySerializer(faculty, many = True)
                return render(request, 'tutor_fac.html', {'faculties':serializer.data})
            except Exception as e:
                print(e)
                return render(request,'tutor_fac.html')
            
        try:
            tutor = Tutor.objects.get(id = pk)
            serializer = TutorSerializer(tutor)
            return render(request, 'tutors-item.html', {'tutor':serializer.data})
        except Exception as e:
                print(e)
                return render(request,'tutors-item.html')
        
class TutorApiView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            try:
                turor = Tutor.objects.all()
                page = Paginator(turor, 9)
                faculty = Faculty.objects.all()
                serializer = FacultySerializer(faculty, many = True)
                return Response({'faculties':serializer.data})
            except Exception as e:
                print(e)
                return Response({403:"ma'lumot topilmadi"})
            
        try:
            tutor = Tutor.objects.get(id = pk)
            serializer = TutorSerializer(tutor)
            return render({'tutor':serializer.data})
        except Exception as e:
                print(e)
                return Response({403:"ma'lumot topilmadi"})

class TutorFilterView(TemplateView):
    def get(self, request, pk):
        try:
            tutor =  Tutor.objects.filter(faculty=pk)
            serializer = TutorSerializer(tutor, many = True)            
            return render(request, 'tutors.html', {'tutor_det':serializer.data})
        except Exception as e:
                print(e)
                return render(request, 'tutors.html')
            


        
        
    
class Indicators(TemplateView):
    def get(self, request):
        url_talabalr = 'https://student.uzfi.uz/rest/v1/public/stat-student'
        url_structure = 'https://student.uzfi.uz/rest/v1/public/stat-structure'
        url_xodimlar = 'https://student.uzfi.uz/rest/v1/public/stat-employee'
        response_talabalar = requests.get(url_talabalr).json()
        response_structure = requests.get(url_structure).json()
        response_xodimlar = requests.get(url_xodimlar).json()

        indicators = {
            "response_talabalar": response_talabalar["data"]["education_type"]["Jami"],
            "response_structure": response_structure["data"]["departments"],
            "response_xodimlar": response_xodimlar["data"]["employment_form"],
            "response_uqtuvchilar": response_xodimlar["data"]["position"]
        }

        return Response(indicators)