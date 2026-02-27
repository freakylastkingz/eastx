
from django.contrib import admin
from django.urls import path

from formapp.views import index, success

urlpatterns = [
    path('', index, name='index'),
    path('success/', success, name='success'),
    path('admin/', admin.site.urls),
]
