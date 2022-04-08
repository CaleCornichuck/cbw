"""from django.urls import path"""
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.OperationalSecurityTab_list),
    path('Dirbuster',views.DirbusterTab_list, name="dirbuster"),
    path('Stegnography',views.StegnographyTab_list, name="stegnography"),
]


