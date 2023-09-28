from log.models import (User, Teacher, Grade, Manager, Program, Student)
from rest_framework.decorators import action
from log.logserializers import (
    UserSerializer,
    TeacherSerializer,
    GradeSerializer,
    ManagerSerializer,
    ProgramSerializer,
    StudentSerializer,
    )
from rest_framework import generics,views
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import mixins

from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import viewsets, mixins

class UserModelViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    """api views for users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @csrf_exempt
    @action(detail=True, methods=['POST'])
    def new_user(self, request):
        # Check if user with the same data already exists
        username = request.data.get('username')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Return the created user data
        # return Response(serializer.errors, status=400)

class TeacherModelViewSet(viewsets.ModelViewSet):
    """model view set"""
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class GradeViews(viewsets.ModelViewSet):
    """models view for grade"""
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class ManagerView(viewsets.ModelViewSet):
    """models view for Managers"""
    serializer_class =ManagerSerializer
    queryset = Manager.objects.all()


class ProgramView(viewsets.ModelViewSet):
    """models for Programme of study"""
    serializer_class=ProgramSerializer
    queryset = Program.objects.all()

class StudentView(viewsets.ModelViewSet):
    """models for students"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()