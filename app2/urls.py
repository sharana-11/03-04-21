from django.urls import path
from app1 import views
app_name="app2"

urlpatterns = [
    path('index2/', views.index,name="index"),
    path('sample2/',views.sample2,name="sample2"),
]