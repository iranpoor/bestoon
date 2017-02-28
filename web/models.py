

from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Token = models.CharField(max_length=48)

    def __str__(self):
        return "{}_Token".format(self.User)


# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)



class income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    def  __str__ (self):
        return  "{}-{}" .format(self.date, self.amount)
