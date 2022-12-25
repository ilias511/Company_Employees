from django.db import models

# Create your models here.

COMPANY_MAX_LENGTH = 25

EMPLOYEE_POSITION = [
("CEO", "CEO"),
    ("Director", "Director"),
    ("Manager", "Manager"),
    ("HR", "HR"),
    ("Accountant","Accountant"),
    ("Developer","Developer")

]

EMPLOYEE_POSITION_MAX_LENGTH = 100


class Company(models.Model):
    name = models.CharField(max_length=COMPANY_MAX_LENGTH)
    logo = models.URLField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.URLField()
    position = models.CharField(max_length=EMPLOYEE_POSITION_MAX_LENGTH,choices=EMPLOYEE_POSITION)
    salary = models.IntegerField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.company.name

