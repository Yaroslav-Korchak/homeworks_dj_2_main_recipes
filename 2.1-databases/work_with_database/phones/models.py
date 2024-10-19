from django.db import models


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)
