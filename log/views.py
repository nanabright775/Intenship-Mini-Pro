from log.models import (User, Teacher, Grade,
                        Manager, Program, Student,
                        LibraryTransaction, Book, Event,
                        Payment, Fee, ParentGuardian, AcademicYear,
                        )
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from log.logserializers import (
    StudentImageSerializer,
    UserSerializer,
    TeacherSerializer,
    GradeSerializer,
    ManagerSerializer,
    ProgramSerializer,
    StudentSerializer,
    FeeSerializer,
    AcademicYearSerializer,
    ParentGuardianSerializers,
    PaymentSerializer,
    EventSerializer,
    BookSerializer,
    LibraryTransactionSerializer,
    StudentDetailSerialiser,
    )
from rest_framework import generics,views
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins

from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import viewsets, mixins

class UserModelViewSet(viewsets.ModelViewSet):
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
    #serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def get_serializer_class(self):
        """return the serializer class for request"""
        if self.action == 'list':
            return StudentSerializer
        elif self.action=='upload_image':
            return StudentImageSerializer
        return self.serializer_class
    
    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """function for uploading image to recipe"""
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    

class LibraryTransactionView(viewsets.ModelViewSet):
    """library view set"""
    serializer_class = LibraryTransactionSerializer
    queryset = LibraryTransaction.objects.all()

class BookView(viewsets.ModelViewSet):
    """book view set"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class EventView(viewsets.ModelViewSet):
    """event view"""
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class PaymentView(viewsets.ModelViewSet):
    """payment view """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class FeeView(viewsets.ModelViewSet):
    """fees view set"""
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()

class ParentGuardianView(viewsets.ModelViewSet):
    """parent/guardian viewset"""
    serializer_class = ParentGuardianSerializers
    queryset = ParentGuardian.objects.all()

class AcademicYearView(viewsets.ModelViewSet):
    """academicyear view"""
    serializer_class = AcademicYearSerializer
    queryset = AcademicYear.objects.all()
    
class StudentDetailView(viewsets.ModelViewSet):
    """viewset for student detail view"""
    serializer_class = StudentDetailSerialiser
    queryset=Student.objects.all()