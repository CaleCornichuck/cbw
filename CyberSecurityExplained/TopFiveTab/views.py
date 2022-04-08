from django.shortcuts import render

# Create your views here.
def TopFiveTab_list(request):
    return render(request, 'TopFiveTab/TopFiveTab_list.html')

def PhishingTab_list(request):
    return render(request, 'TopFiveTab/PhishingTab_list.html')

def MalRansomwareTab_list(request):
    return render(request, 'TopFiveTab/MalRansomwareTab_list.html')

def InsiderThreatsTab_list(request):
    return render(request, 'TopFiveTab/InsiderThreatsTab_list.html')

def DDOSTab_list(request):
    return render(request, 'TopFiveTab/DDOSTab_list.html')

def IOTSQLTab_list(request):
    return render(request, 'TopFiveTab/IOTSQLTab_list.html')