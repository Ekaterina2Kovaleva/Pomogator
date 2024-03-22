from django.contrib.auth.models import User
from django.db import models

from event.models import Event



class Role(models.Model):
    name = models.CharField(verbose_name='Роль', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to ='uploads/')
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True, null=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, null=True, blank=True)
    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.CASCADE, null=True, blank=True)
    group = models.CharField(verbose_name='Группа', max_length=10, null=True, blank=True)
    vk = models.CharField(verbose_name='ВКонтакте', max_length=10, null=True, blank=True)
    tg = models.CharField(verbose_name='Telegram', max_length=10, null=True, blank=True)
    birthday = models.DateField(verbose_name='День рождения', null=True, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', max_length=255, blank=True, unique=True)
    gmail = models.EmailField(verbose_name='Электронная почта Google', max_length=255, blank=True, unique=True)

