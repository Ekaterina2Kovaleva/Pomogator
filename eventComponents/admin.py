from django.contrib import admin
from .models import Task, Status, Type_Link, Link

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Type_Link)
admin.site.register(Link)
