from django.shortcuts import render

# Create your views here.
def CostBenefitTab_list(request):
    return render(request, 'CostBenefitTab/CostBenefitTab_list.html')