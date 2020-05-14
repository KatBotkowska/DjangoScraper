from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework import views
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import JobOffert
from .serializers import JobOffertSerializer


class JobOffertViewSet(ListAPIView):
    queryset = JobOffert.objects.all()
    serializer_class = JobOffertSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('keywords',)
    filter_fields = ('city', 'company', 'still_active', 'job_service')
    ordering = ('city')


class SingleJobOffertView(RetrieveAPIView):
    queryset = JobOffert.objects.all().order_by('city', 'title')
    serializer_class = JobOffertSerializer


class CityView(ListAPIView):
    serializer_class = JobOffertSerializer
    filter_fields = ('still_active', 'job_service')
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('keywords',)
    ordering = ('job_service')

    def get_queryset(self):
        queryset = JobOffert.objects.all().order_by('city', 'title')
        city = self.kwargs.get('city')
        if city:
            queryset = queryset.filter(city__iexact=city)
        return queryset


class ServiceView(ListAPIView):
    serializer_class = JobOffertSerializer
    filter_fields = ('still_active','city', 'company')
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('keywords',)
    ordering = ('city')

    def get_queryset(self):
        queryset = JobOffert.objects.all()
        service = self.kwargs.get('service')
        if service:
            queryset = queryset.filter(job_service__iexact=service)
        return queryset


class TechView(ListAPIView):
    serializer_class = JobOffertSerializer
    filter_fields = ('city', 'company','still_active', 'job_service')
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('title',)
    ordering = ('job_service')

    def get_queryset(self):
        queryset = JobOffert.objects.all()
        tech = self.kwargs.get('technology')
        if tech:
            queryset = queryset.filter(keywords__icontains=tech)
        return queryset
