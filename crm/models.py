from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta():
        ordering = ['-date_created']

    def __str__(self):
        return self.name

    def get_absolute_url():
        return reverse("crm-detail" , kwargs={"pk":self.id})

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField()
    total_amount = models.FloatField()
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta():
        ordering = ['-date_created']


class Lead(models.Model):

    STATUS = (
        ("Open","Open"),
        ("Close","Close"),
        ("No Response","No Response"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)
    Quantity = models.FloatField()
    total_amount = models.FloatField()
    description = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    target = models.FloatField(null=True)

