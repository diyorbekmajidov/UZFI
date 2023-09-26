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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DekanSerializer(serializers.ModelSerializer):
    # dekan = UserSerializer(read_only=True)
    class Meta :
        model = Dekan
        fields = '__all__'
        

    # def get_dekan(self, obj):
    #     print(obj.dekan.id)
    #     return obj.dekan.username
    
    
        
