from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.TopFiveTab_list),
    path('Phishing',views.PhishingTab_list, name="phishing"),
    path('MalRansomware',views.MalRansomwareTab_list, name="mal/ransomware"),
    path('InsiderThreats',views.InsiderThreatsTab_list, name="insider threats"),
    path('IOTSQL',views.IOTSQLTab_list, name="iot/sql"),
    path('DDOS',views.DDOSTab_list, name="ddos"),
]


