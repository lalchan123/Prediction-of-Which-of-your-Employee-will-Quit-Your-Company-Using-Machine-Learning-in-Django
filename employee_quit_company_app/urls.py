from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predict/', views.predict, name="predict"),
    path('predict/result/', views.result, name="result"),
    path('predict/result/recordData/', views.recordData, name="recordData"),
]
