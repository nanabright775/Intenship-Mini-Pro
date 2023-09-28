from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify



class User(AbstractUser):
    """abstract user from django provided user"""
    is_teacher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    """models for school data"""
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact_number = models.BigIntegerField
    address=models.TextField(blank=True)
    date_of_birth = models.DateField
    password = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_teacher = True
        user.save()
        super().save(*args, **kwargs)
    def get_courses(self):
        return self.course_set.all()
    def _str_(self):
        return self.name.username


class AcademicYear(models.Model):
    """Academic Year Database"""
    academic_year_name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.academic_year_name



class Grade(models.Model):
    """creating grade model"""
    academicYear=models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
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
    """models for school manager"""
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact_number = models.BigIntegerField
    address=models.TextField(blank=True)
    date_of_birth = models.DateField
    password = models.CharField(max_length=100)
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


class ParentGuardian(models.Model):
    """models for guardian"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    relationship_to_student = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    """models for students"""
    parentGuardian=models.ForeignKey(ParentGuardian, on_delete=models.CASCADE)
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=2)
    contact_number = models.BigIntegerField
    address=models.TextField(blank=True)
    date_of_birth = models.DateField
    def save(self, *args, **kwargs):
        user = User.objects.get(username=self.name.username)
        user.is_student = True
        user.save()
        super().save(*args, **kwargs)
    # def get_courses(self):
    #     return self.course_set.all()
    def __str__(self):
        return self.name.username


class Fee(models.Model):
    """models for fees"""
    academicyear=models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description

class Payment(models.Model):
    """models for payment"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.student} paid {self.amount_paid} for {self.fee}"


class Event(models.Model):
    """models for events"""
    academicYear=models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name

class Book(models.Model):
    """models for books"""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class LibraryTransaction(models.Model):
    """models for transactons at the library"""
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} checked out {self.book}"