from django.contrib import admin
from django.urls import path
from home.views import first_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',first_views,name ='home')
]
