from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    full_name=models.CharField(max_length=50)
    employee_code=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    def __str__(self):
        return self.employee_code
    def __str__(self):
        return self.mobile_no




