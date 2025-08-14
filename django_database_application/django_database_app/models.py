from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"