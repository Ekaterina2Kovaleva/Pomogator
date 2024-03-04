from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
