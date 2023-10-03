from rest_framework import serializers
from .models.models import *


class CharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charter
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Document
        fields = '__all__'

class CouncilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Councils
        fields = '__all__'

class RequisitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisites
        fields = '__all__'

class FinancialStatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialStatements
        fields = '__all__'

class OpenDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenData
        fields = '__all__'

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class FacultySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']

class DirectionSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer1()
    class Meta:
        model = Direction
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "role"]
        

class DekanSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Dekan
        fields = "__all__"

class GetDekanSerializer(serializers.ModelSerializer):
    dekan = UserSerializer1()
    faculty = FacultySerializer1()
    class Meta :
        model = Dekan
        fields = ["id", "dekan", "faculty", "name", "img", "phone","address_uz","address_en","address_ru", 
                  "acceptance_uz","acceptance_ru","acceptance_en","duties_uz","duties_ru","duties_en",
                  "date_created", "date_update",
                  ]
        depth = 2

class KafedraManagerSerializer(serializers.ModelSerializer):
    class Meta :
        model = KafedraManager
        fields = "__all__"
        # depth = 2
        

class GetKafedraManagerSerializer(serializers.ModelSerializer):
    kafedramanager = UserSerializer1()

    class Meta :
        model = KafedraManager
        fields = ["id", "kafedramanager", "name", "img", "phone","address_uz","address_en","address_ru", 
                  "acceptance_uz","acceptance_ru","acceptance_en","duties_uz","duties_ru","duties_en",
                  "date_created", "date_update",
                  ]
        depth = 2

