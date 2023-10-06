from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import Dekan
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class AllDekan(ListCreateAPIView):
    queryset = Dekan.objects.all()
    serializer_class = GetDekanSerializer
class GetDekanById(APIView):
    def get(self, request, pk):
        data = Dekan.objects.get(id=pk)
        serializers = GetDekanSerializer(data)
        return Response(serializers.data)

class DekanApiview(APIView):
    @swagger_auto_schema(
        request_body=DekanSerializer,
        operation_description='''Create Dekan:User yaratilgan bulishi lozim. data ni str kurinishda yuborish kerak dekan  name id emas,
        faculty ham huddi shu kurinishda''',
        responses={
            200: 'User crate dekan'
        }
    )

    def post(self, request):
            data = request.data
            dekan = request.data['dekan']
            faculty = request.data['faculty']
            role = User.objects.get(username=dekan).role
            if role == 'DEKAN':
                data['faculty'] = Faculty.objects.get(name=faculty).id
                data['dekan'] = User.objects.get(username=dekan).id
                # print(data)
                serializer = DekanSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Sizning role noto\'g\'ri'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class DekanGetApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # @swagger_auto_schema(
    #      request_body = GetDekanSerializer,
    #      operation_description = '''Dekanni get qilish uchun, token yuborish kerak usha dekan malumotlari qaytadi.
    #        Va undan tashqari dekan update va dekan delet''',
    #      responses = {
    #          200: 'Dekanni get qilish'
    #      }
    #      )

    def get(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        serializers = GetDekanSerializer(dekan)
        return Response(serializers.data)
    
    def put(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        serializer = DekanSerializer(dekan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        dekan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    