from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def OperationalSecurityTab_list(request):
    return render(request,'OperationalSecurityTab/OperationalSecurityTab_list.html')

def DirbusterTab_list(request):
    return render(request, 'OperationalSecurityTab/DirbusterTab_list.html')

def StegnographyTab_list(request):
    return render(request, 'OperationalSecurityTab/StegnographyTab_list.html')
