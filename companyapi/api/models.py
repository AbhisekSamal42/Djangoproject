from django.db import models

# Creating company model.

class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),('CORE','CORE')))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.name +'--'+ self.location
    


# Creating employees model.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),('Developer','Developer'),('Software tester','Software tester'),('Jr. developer','Jr. developer')))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
