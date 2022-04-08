from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.CryptographyTab_list),
    path('Hashcat',views.HashcatTab_list, name="hashcat"),
    path('JohntheRipper',views.JohntheRipperTab_list, name="john")
]


