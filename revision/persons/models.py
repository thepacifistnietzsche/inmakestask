from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    Name = models.CharField(max_length=250)
    DOB = models.DateTimeField()
    Age = models.IntegerField()
    Phone_number = models.IntegerField()
    email = models.EmailField()
    Gender = models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    Documents = models.CharField(max_length=250)
    Account_type = models.CharField(max_length=250)
    def __str__(self):
        return self.name