from rest_framework import serializers
from log.models import (
    User, Teacher, Grade, Manager,
    Student, Program, LibraryTransaction, Fee,
    Payment, Event, Book, LibraryTransaction, ParentGuardian, AcademicYear)

class UserSerializer(serializers.ModelSerializer):
    """serializers for users"""
    class Meta:
        model = User
        fields = ['username','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Make the 'password' field write-only
        }

class TeacherSerializer(serializers.ModelSerializer):
    """serializers for teachers"""
    name = UserSerializer
    class Meta:
        model = Teacher
        fields =['name', 'contact_number', 'address', 'date_of_birth', 'image']

class GradeSerializer(serializers.ModelSerializer):
    """serializers for grades"""
    class Meta:
        model = Grade
        fields = ['name', 'code',]


class ManagerSerializer(serializers.ModelSerializer):
    """serializers for managers"""
    name = UserSerializer
    class Meta:
        model = Manager
        fields = ['name', 'contact_number', 'address', 'date_of_birth',  'image']



class ProgramSerializer(serializers.ModelSerializer):
    """serializers for programs"""
    teacher = TeacherSerializer
    grade = GradeSerializer
    manager = ManagerSerializer
    class Meta:
        model = Program
        fields = ['subject', 'abb', 'teacher', 'grade', 'manager']

class StudentSerializer(serializers.ModelSerializer):
    """serializers for students"""
    name=UserSerializer
    grade = GradeSerializer
    class Meta:
        model = Student
        fields = ['name', 'grade',]


class AcademicYearSerializer(serializers.ModelSerializer):
    """serializers for Academics"""
    class Meta:
        model = AcademicYear
        fields =['academic_year_name', 'start_date', 'end_date']

class ParentGuardianSerializers(serializers.ModelSerializer):
    """serializers for parents"""
    class Meta:
        model = ParentGuardian
        fields = ['first_name', 'last_name', 'email', 'relationship_to_student']


class FeeSerializer(serializers.ModelSerializer):
    """serialozers for Fee"""
    academicyear=AcademicYearSerializer
    student = StudentSerializer
    class Meta:
        model = Fee
        fields =['academicyear', 'student', 'description', 'amount']

class PaymentSerializer(serializers.ModelSerializer):
    """serializers for payment"""
    student = StudentSerializer
    fee = FeeSerializer
    class Meta:
        model = Payment
        fields = ['student', 'fee', 'payment_date', 'amount_paid']



class EventSerializer(serializers.ModelSerializer):
    """model serializer for event"""
    academinyear=AcademicYearSerializer
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'location', 'organizer']



class BookSerializer(serializers.ModelSerializer):
    """model serializer"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available', 'image']


class LibraryTransactionSerializer(serializers.ModelSerializer):
    """serializer for library transactions"""
    academicyear=AcademicYearSerializer
    book = BookSerializer
    student = StudentSerializer
    class Meta:
        model = LibraryTransaction
        fields = ['academicyear', 'book', 'student', 'checkout_date', 'return_date']

class  ParentOrGuardianSerializer(serializers.ModelSerializer):
    """serializer for parentGuardian serializer"""
    class Meta:
        model = ParentGuardian
        fields = ['first_name', 'last_name', 'email', 'relationship_to_student']
        
class StudentImageSerializer(serializers.ModelSerializer):
    """serializer for uploading student images"""
    class Meta:
        model = Student
        fields =['image', ]
        read_only_fields=['id']
        extra_kwargs = {'image': {'required': 'True'}}
        
class StudentDetailSerialiser(serializers.ModelSerializer):
    """students detail serializer"""
    name = UserSerializer
    grade = GradeSerializer
    parentGuardian = ParentOrGuardianSerializer
    image = StudentImageSerializer
    
    class Meta:
        model = Student
        fields = ['name', 'grade', 'parentGuardian', 'image', 'contact_number', 'address', 'date_of_birth']