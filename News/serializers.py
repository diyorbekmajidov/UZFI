from rest_framework import serializers
from .models import *


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'

class NewsContentSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = News_Content
        fields = '__all__'

    def get_category(self, obj):
        return [x.new_category for x in obj.category.all() ]
    

class UserNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Content
        fields = '__all__'