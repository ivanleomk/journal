from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myacc/',views.account,name='account'),
    path('entries/',views.entries,name='entries'),
]
