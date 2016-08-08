from django.db import models

import datetime
from django.utils import timezone

class MaterialTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(MaterialTag, blank=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ShortSize(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published")
    description = models.TextField(default="")
    material = models.ForeignKey(Material, null=True)
    color = models.ForeignKey(Color, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default='0000.00')
    short_size = models.ForeignKey(ShortSize, null=True)
    image = models.ImageField(null=True)
    short_url = models.CharField(max_length=200, null=True, unique=True)

class Company(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date_added")
    blurb = models.CharField(max_length=250, default="")
    address_line_1 = models.CharField(max_length=1000, default="")
    address_line_2 = models.CharField(max_length=1000, default="")
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    image = models.ImageField(null=False)
    caption = models.CharField(max_length=250, null=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    # todo: tags on photos

    def __str__(self):
        return self.name








# Create your models here.
