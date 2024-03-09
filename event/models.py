from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Окончание мероприятия')
    users = models.ManyToManyField(User, verbose_name='Участники')

    def __str__(self):
        return self.title


class Point(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Название ключевой точки мероприятия')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='Дата и Время', null=True, blank=True)

    def __str__(self):
        return self.title