"""from django.urls import path"""
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.ResourcesTab_list),
]


