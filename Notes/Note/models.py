from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    full_text = models.TextField()
    create_date = models.DateTimeField()
    change_date = models.DateTimeField()
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    url = models.SlugField(max_length=100)
    url_access = models.BooleanField(default=False)
