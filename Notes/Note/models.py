from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    full_text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    change_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменнения')
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    url = models.SlugField(verbose_name="Идентификатор", max_length=100)
    url_access = models.BooleanField(default=False)

    def __str__(self):
        return self.title
