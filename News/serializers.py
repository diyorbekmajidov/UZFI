from rest_framework import serializers
from .models import *

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"

class NewsContentSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = News_Content
        fields = '__all__'

    def get_category(self, obj):
        return [{"category":x.new_category, "id":x.id} for x in obj.category.all() ]
    

class UserNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Content
        fields = '__all__'

class PopularStudentImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularStudentImg
        fields = ["img"]
class PopularStudentsSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = PopularStudents
        fields = ["id","student_name","body","description","img"]

    def get_img(self, obj):
        image = PopularStudentImg.objects.filter(popular=obj.id)
        if image:
            return PopularStudentImgSerializer(image, many=True).data
        else:
            return None

class VedioNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vedio_New
        fields = "__all__"

class PendingEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingEvents
        fields = "__all__"