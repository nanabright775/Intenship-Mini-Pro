from django.contrib import admin
from log import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Manager)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Grade)
admin.site.register(models.Program)