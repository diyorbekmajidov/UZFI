from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UZFI.models.models import *
from UZFI.serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DekanApiview(APIView):
    def post(self, request):
        data = request.data
        dekan = request.data['dekan']
        faculty = request.data['faculty']
        role = User.objects.get(username=dekan).role
        if role == 'DEKAN':
            data['faculty'] = Faculty.objects.get(name=faculty).id
            data['dekan'] = User.objects.get(username=dekan).id
            serializer = DekanSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Sizning role noto\'g\'ri'}, status=status.HTTP_400_BAD_REQUEST)
    
class DekanGetApiview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dekan = Dekan.objects.get(dekan=request.user)
        print(dekan.faculty)
        serializers = DekanSerializer(dekan)
        return Response(serializers.data)