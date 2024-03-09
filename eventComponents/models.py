from django.contrib.auth.models import User
from django.db import models
from event.models import Event


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус задания')

    def __str__(self):
        return self.name


class Type_Link(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип ссылки')

    def __str__(self):
        return self.name


class Link(models.Model):
    link = models.CharField(max_length=10000, verbose_name='Название ссылки')
    name = models.CharField(max_length=1000, verbose_name='Ссылка')
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE)
    type = models.ForeignKey(Type_Link, on_delete=models.CASCADE, verbose_name='Тип ссылки')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=10000, verbose_name='Описание')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Готовность')
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name='Ответсвенный', on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.title

