from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Site

def SearchTab_list(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = Site.objects.filter(name__icontains=searched)
        return render(request,'SearchTab/SearchTab_list.html', {'searched':searched, 'results':results})
    else:
        return render(request,'SearchTab/SearchTab_list.html')