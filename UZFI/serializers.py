from rest_framework import serializers
from .models import *


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

class ScientificWorkSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ScientificWork
        fields = '__all__'      

class DekanSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Dekan
        fields = "__all__"

class GetDekanSerializer(serializers.ModelSerializer):
    dekan = UserSerializer1()
    faculty = FacultySerializer1()
    # scientific_work = ScientificWorkSerializer()
    class Meta :
        model = Dekan
        fields = '__all__'

class KafedraSerializer(serializers.ModelSerializer):
    class Meta :
        model = Kafedra
        fields = "__all__"

class KafedraSerializer1(serializers.ModelSerializer):
    class Meta :
        model = Kafedra
        fields = ["id", "name"]

class KafedraManagerSerializer(serializers.ModelSerializer):
    class Meta :
        model = KafedraManager
        fields = "__all__"
        

class GetKafedraManagerSerializer(serializers.ModelSerializer):
    kafedramanager = UserSerializer1()
    kafedra = KafedraSerializer1()
    scientific_work = ScientificWorkSerializer()
    class Meta :
        model = KafedraManager
        fields = "__all__"

