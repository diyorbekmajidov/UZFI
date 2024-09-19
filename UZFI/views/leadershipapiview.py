from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from UZFI.models import *
from UZFI.serializers import *
from django.shortcuts import render

class LeadershipAPIView(TemplateView):
    def get(self, request):
        try :
            leadership = Leadership.objects.all().order_by('number')
            serializers = LeadershipSerializer(leadership, many=True)
            return render(request, 'leadership.html',{"data":serializers.data})
        except Exception as e:
            return render(request, 'leadership.html')
        
class LeadershipByIdAPIView(TemplateView):
    def get(self, request, pk):
        try :
            leadership = Leadership.objects.get(id=pk)
            serializers = LeadershipSerializer(leadership)
            user = leadership.rector.id
            scientifi_work = ScientificWork.objects.filter(user=user)
            serializers1 = ScientificWorkSerializer(scientifi_work, many = True)
            return render(request, 'leadership-item.html',{
                "data":serializers.data,
                "scientificwork":serializers1.data
                })
        except Exception as e:
            print(e)
            return render(request, 'leadership-item.html')