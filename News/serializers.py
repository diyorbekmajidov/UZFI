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
    
class NewsBycotegorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        models = News_Content
        fields = ('id','category', 'news_title','news_content')

    def get_category(self, obj):
        categories = obj.category.all()
        return [category.name for category in categories]
class UserNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Content
        fields = '__all__'