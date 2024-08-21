from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    first_semester_grade = models.FloatField()
    second_semester_grade = models.FloatField()
    professor_name = models.CharField(max_length=100)
    classroom_number = models.IntegerField()
    
def __str__(self):
        return self.name
