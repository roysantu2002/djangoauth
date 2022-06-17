from FirstApp.models import Departments
from FirstApp.serializers import DepartmentSerializer
from rest_framework import viewsets


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.order_by('-DepartmentId')
    serializer_class = DepartmentSerializer
