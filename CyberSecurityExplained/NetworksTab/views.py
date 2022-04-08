from django.shortcuts import render

# Create your views here.
def NetworksTab_list(request):
    return render(request, 'NetworksTab/NetworksTab_list.html')

def WiresharkTab_list(request):
    return render(request, 'NetworksTab/WiresharkTab_list.html')

def WifiPineappleTab_list(request):
    return render(request, 'NetworksTab/WifiPineappleTab_list.html')
