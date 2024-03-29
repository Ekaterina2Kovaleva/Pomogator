from django.contrib import admin
from . import models
from .models import Role, AuthUser

admin.site.register(Role)
admin.site.register(AuthUser)


