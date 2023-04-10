from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(default=datetime.now, null=True, blank=True)
    end_date= models.DateField()

    def __str__(self):
        return f'{self.category} - {self.limit}'

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE,default=1)
    reason = models.TextField(blank=True, null=True)
    left = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(default=datetime.now, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f'{self.category} - {self.amount}'


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_expenses= models.DecimalField(max_digits=100, decimal_places=2)
    budget_left= models.DecimalField(max_digits=100, decimal_places=2)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
