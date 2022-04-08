from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def ResourcesTab_list(request):
    return render(request,'ResourcesTab/ResourcesTab_list.html')