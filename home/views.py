from django.shortcuts import render

# Create your views here.


def first_views(request):
    return render(request,'index.html')