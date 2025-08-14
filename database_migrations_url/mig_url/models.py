from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField()
    date_of_birth = models.DateField()

# This function shows which thing you want to display in django admin or django shell
    def __str__(self):
        return self.name
    
    
    