# Generated by Django 4.2.15 on 2024-09-20 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machine_learning', '0008_alter_userprogress_options_alter_workout_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sex', models.CharField(max_length=10)),
                ('Age', models.PositiveIntegerField()),
                ('Height', models.FloatField()),
                ('Weight', models.FloatField()),
                ('Hypertension', models.CharField(max_length=3)),
                ('Diabetes', models.CharField(max_length=3)),
                ('BMI', models.FloatField()),
                ('Level', models.CharField(max_length=50)),
                ('Fitness_Goal', models.CharField(max_length=50)),
                ('Fitness_Type', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'List of User Profiles',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
