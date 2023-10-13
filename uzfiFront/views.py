from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.


class Index(View):
    def get(self, req:HttpRequest, *args, **kwargs):
        return render(req, 'index.html')