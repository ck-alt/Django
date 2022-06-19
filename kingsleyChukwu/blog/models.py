from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

user = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(auto_now_add=True)


    