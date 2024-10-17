from django.db import models
from django.contrib.auth.models import User


class Condition(models.Model):
    condition = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Condition"

    def __str__(self):
        return self.condition



class Category(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category


class Cars(models.Model):
    model = models.CharField(max_length=25)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=1000)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.model


class Car(models.Model):
    model = models.CharField(max_length=25)
    year = models.IntegerField()
    brand = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=1000, help_text='Enter Image Link')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Car"


    def __str__(self):
        return self.model



