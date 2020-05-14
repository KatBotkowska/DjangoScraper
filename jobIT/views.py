from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework import views
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from url_filter.integrations.drf import DjangoFilterBackend
#from django_filters.rest_framework import DjangoFilterBackend
from .models import JobOffert
from .serializers import JobOffertSerializer


class JobOffertViewSet(viewsets.ModelViewSet):
    queryset = JobOffert.objects.all()
    serializer_class = JobOffertSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('keywords',)
    filter_fields = ('city', )
    #filter_fields = ('city', 'company', 'still_active', 'job_service')
    ordering = ('city')



class SingleJobOffertView(RetrieveAPIView):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer


class CityView(ListAPIView):
    # queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ('city', 'company')

    # filterset_fields = ('city')
    # model = JobOffert
    def get_queryset(self):
        queryset = JobOffert.objects.all().order_by('city', 'title')
        city = self.kwargs.get('city')
        # city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city__iexact=city)
        return queryset


class ServiceView(ListAPIView):
    serializer_class = JobOffertSerializer
    filter_fields = ('city', 'company')

    def get_queryset(self):
        queryset = JobOffert.objects.all().order_by('city', 'title')
        service = self.kwargs.get('service')
        if service:
            queryset = queryset.filter(job_service__iexact=service)
        return queryset


class TechView(ListAPIView):
    serializer_class = JobOffertSerializer
    filter_fields = ('city', 'company')

    def get_queryset(self):
        queryset = JobOffert.objects.all().order_by('city', 'title')
        tech = self.kwargs.get('technology')
        if tech:
            queryset = queryset.filter(keywords__icontains=tech)
        return queryset
