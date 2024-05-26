from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    hallticket_number=models.CharField(max_length=10)
    Marks=models.CharField(max_length=3)
    Grade=models.CharField(max_length=2)
    Result=models.CharField(max_length=5)
    def __str__(self):
        return self.Name

