# import serializer from rest_framework
from rest_framework import serializers

from FirstApp.models import Departments


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=['DepartmentId','DepartmentName',]
