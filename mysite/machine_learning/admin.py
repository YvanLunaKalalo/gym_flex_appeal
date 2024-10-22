from django.contrib import admin
from .models import Workout, UserProfile, UserProgress

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Desc', 'Type', 'BodyPart', 'Equipment', 'Level')
    search_fields = ('Title', 'Desc', 'Type', 'BodyPart', 'Equipment', 'Level')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'Sex', 'Age', 'Height', 'Weight', 'BMI', 'Fitness_Goal', 'Fitness_Type')
    search_fields = ('user__username', 'Sex', 'Fitness_Goal', 'Fitness_Type')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout', 'progress', 'date', 'progress_date')
    search_fields = ('user__username', 'workout__Title')

