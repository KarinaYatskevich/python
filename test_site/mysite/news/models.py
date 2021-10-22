from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    another_title = models.CharField(max_length=150)
    bibliographic_entry = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    abstract_in_another_language = models.TextField(blank=True)
    URL = models.URLField()
    authors = models.TextField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    likes = models.ManyToManyField(User, related_name='news_posts')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    def total_likes(self):
        return self.likes.count()

    def is_favourite(self):
        return self.favourite.count()

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

