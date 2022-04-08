from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def CatWebsiteApplication(request):
    return render(request, 'CatWebsiteApplication/homepage.html')
    
