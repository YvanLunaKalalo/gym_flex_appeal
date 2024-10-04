from django.urls import path
from . import views

urlpatterns = [
    path('bmi/', views.bmi_view, name="bmi"),
    path('workout/', views.workout_view, name="workout"),
    path('recommend_workout/', views.recommended_workout_view, name='recommend_workout'),
    path('recommend/', views.workout_recommendation_view, name="recommend"),
    path('workout-recommendations/', views.workout_recommendation_view, name='workout_recommendations'),
    path('progress/<str:workout_title>/', views.update_progress_view, name='update_progress'),
]