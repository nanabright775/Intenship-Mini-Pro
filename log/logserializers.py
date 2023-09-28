from rest_framework import serializers
from log.models import User, Teacher, Grade, Manager, Student, Program

class UserSerializer(serializers.ModelSerializer):
    """serializers for users"""
    class Meta:
        model = User
        fields = ['username','email', 'password']

class TeacherSerializer(serializers.ModelSerializer):
    """serializers for teachers"""
    name = UserSerializer
    class Meta:
        model = Teacher
        fields =['name']

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
        fields = ['name']



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
        fields = ['name', 'grade']
