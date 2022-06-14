from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

from FirstApp import views

urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
