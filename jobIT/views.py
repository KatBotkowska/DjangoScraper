from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import views
from rest_framework.generics import RetrieveAPIView

from .models import JobOffert
from .serializers import JobOffertSerializer

class JobOffertViewSet(viewsets.ModelViewSet):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer

class SingleJobOffertView(RetrieveAPIView):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer


