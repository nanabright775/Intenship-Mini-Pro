from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from log import views


router = DefaultRouter()
router.register('teacher', views.TeacherModelViewSet)
router.register('grade', views.GradeViews)
router.register('manager', views.ManagerView)
router.register('program', views.ProgramView)
router.register('student', views.StudentView)
router.register('user', views.UserModelViewSet)

app_name = 'log'

urlpatterns = [
    path('', include(router.urls)),
]