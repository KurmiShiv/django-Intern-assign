from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.db.models import Q
from .models import Artist
from rest_framework import serializers
from .serializers import ArtistSerializer
from rest_framework import generics
from .models import Work
from .serializers import WorkSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkFilteredList(generics.ListAPIView):
    serializer_class = WorkSerializer

    def get_queryset(self):
        work_type = self.request.query_params.get('work_type')
        return Work.objects.filter(work_type=work_type)



class ArtistSearch(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        query = self.request.query_params.get('artist')
        return Artist.objects.filter(Q(name__icontains=query))



@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken.'}, status=status.HTTP_409_CONFLICT)

    user = User.objects.create_user(username=username, password=password)
    return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
