from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import views
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
import django_filters.rest_framework
from .models import JobOffert
from .serializers import JobOffertSerializer

class JobOffertViewSet(viewsets.ModelViewSet):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer

class SingleJobOffertView(RetrieveAPIView):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer


class CityView(viewsets.ModelViewSet):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ('city', 'company')
    # filterset_fields = ('city')
    # model = JobOffert
    # def get_queryset(self):
    #     queryset = JobOffert.objects.all().order_by('city', 'title')
    #     city = self.request.query_params.get('city')
    #     if city:
    #         queryset = queryset.filter(city=city)
    #     return queryset

