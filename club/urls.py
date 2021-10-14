from django.contrib import admin
from django.urls import path,include
from club import views

app_name='club'

urlpatterns=[
    path('real-madrid/', views.real_madrid, name="real-madrid"),

]