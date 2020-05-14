from rest_framework import serializers
from .models import JobOffert


class JobOffertSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="jobIT:job_offert")
    class Meta:
        model = JobOffert
        fields = '__all__'