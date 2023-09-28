from typing import Iterable, Optional
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
# from Course.models import Grade



class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=100)
    access_token = models.CharField(max_length=3000)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_teacher = True
        user.save()
        super().save(*args, **kwargs)
    def get_courses(self):
        return self.course_set.all()
    def _str_(self):
        return self.name.username

class Grade(models.Model):
    """creating grade model"""
    name=models.CharField(max_length=255)
    code=models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def get_courses(self):
        return self._set.all()
    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=100)
    access_token = models.CharField(max_length=3000)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_manager = True
        user.save()
        super().save(*args, **kwargs)
    def get_courses(self):
        return self.course_set.all()
    def _str_(self):
        return self.name.username



class Program(models.Model):
    """creating the course field"""
    subject = models.CharField(max_length=255)
    grade =models.ForeignKey(Grade, on_delete=models.CASCADE)
    abb = models.CharField(max_length= 10,  blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    def save(self, *args , **kwargs):
        if not self.abb:
            self.abb = self.subject[:3]
        super().save(self, *args , **kwargs)
    def __str__(self):
        return self.subject


class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=2)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_student = True
        user.save()
        super().save(*args, **kwargs)
    # def get_courses(self):
    #     return self.course_set.all()
    def __str__(self):
        return self.name.username

