from rest_framework import serializers
from .models import *

class InternationalRelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = InternationalRelation
        fields = "__all__"



class AbiturSerializers(serializers.ModelSerializer):
    class Meta:
        model = Abitur
        fields = "__all__"

class InternationalMemorandumSerializers(serializers.ModelSerializer):
    class Meta:
        model = InternationalMemorandum
        fields = "__all__"

class StudentGroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentGroups
        fields = "__all__"


class InternationalGrantImgerializers(serializers.ModelSerializer):
    class Meta:
        model = InternationalGrantImg
        fields = ["img"]


class InternationalGrantSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = InternationalGrant
        fields = ["id","title","body","img"]

    def get_img(self, obj):
        image = InternationalGrantImg.objects.filter(grant=obj.id)
        if image:
            return InternationalGrantImgerializers(image, many=True).data
        else:
            return None