from rest_framework import serializers
from .models import JobOffert


class JobOffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobOffert
        fields = '__all__'