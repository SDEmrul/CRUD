from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField(max_length=40)
    age=models.IntegerField()
    email=models.EmailField()
    def __str__(self) :
        return f"{self.name} {self.age} {self.email}"