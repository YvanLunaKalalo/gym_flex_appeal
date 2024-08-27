from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('bmi/', views.bmi_view, name="bmi"),
]