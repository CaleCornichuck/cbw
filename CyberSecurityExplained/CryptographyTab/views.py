from django.shortcuts import render

# Create your views here.
def CryptographyTab_list(request):
    return render(request, 'CryptographyTab/CryptographyTab_list.html')

def HashcatTab_list(request):
    return render(request, 'CryptographyTab/HashcatTab_list.html')

def JohntheRipperTab_list(request):
    return render(request, 'CryptographyTab/JohntheRipperTab_list.html')