from django.db import models
from django.urls import reverse

# Create your models here.

class Clothes(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    abstract = models.TextField(blank=True)
    consist = models.CharField(max_length=150)
    care = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos', blank=True)

    def get_absolute_url(self):
        return reverse('clothe_detail', kwargs={'clothe_id': self.pk})

class Category(models.Model):
    title = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    
    def __str__(self):
        return self.title
