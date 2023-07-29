from django.shortcuts import render
from rest_framework import generics
from .models import MandirModel
from .serializers import MandirSerializer
from django.http import HttpResponse
# Create your views here.
class MandirListCreateView(generics.ListCreateAPIView):
    queryset=MandirModel.objects.all()
    serializer_class= MandirSerializer
