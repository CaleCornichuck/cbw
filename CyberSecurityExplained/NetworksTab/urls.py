from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.NetworksTab_list),
    path('Wireshark',views.WiresharkTab_list, name="wireshark"),
    path('WifiPineapple',views.WifiPineappleTab_list, name="wifipine"),
]


