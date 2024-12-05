from django.db import models

# Create your models here.
class Student(models.Model):
    student_date = models.DateField()
    student_time = models.CharField(max_length=100)
    student_duration = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to="static/")
    student_course = models.CharField(max_length=100)
   # py manage.py makemigrations
     # py manage.py migrate