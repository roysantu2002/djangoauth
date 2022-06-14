from urllib import response

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framewok import viewsets
from rest_framework.parsers import JSONParser

from FirstApp.models import Departments
from FirstApp.serializers import DepartmentSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        # return HttpResponse("Hello World!")
        departments = Departments.objects.all()
        # print(departments)
        # return HttpResponse("Hello World!")
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return HttpResponse("Added Successfully")
        return HttpResponse("Failed to Add")
    # elif request.method=='PUT':
    #     department_data=JSONParser().parse(request)
    #     department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
    #     departments_serializer=DepartmentSerializer(department,data=department_data)
    #     if departments_serializer.is_valid():
    #         departments_serializer.save()
    #         return HttpResponse("Updated Successfully",safe=False)
    #     return HttpResponse("Failed to Update")
    # elif request.method=='DELETE':
    #     department=Departments.objects.get(DepartmentId=id)
    #     department.delete()
    #     return HttpResponse("Deleted Successfully",safe=False)
