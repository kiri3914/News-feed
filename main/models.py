from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.IntegerField(default=2)
    biography = models.CharField(max_length=255)

    def __str__(self):
        return self.biography


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image_url = models.ImageField(upload_to='media', blank=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comments(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
