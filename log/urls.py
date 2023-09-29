from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from log import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register('teacher', views.TeacherModelViewSet)
router.register('grade', views.GradeViews)
router.register('manager', views.ManagerView)
router.register('program', views.ProgramView)
router.register('student', views.StudentView)
router.register('user', views.UserModelViewSet)
router.register('academicyear', views.AcademicYearView)
router.register('parentguardian', views.ParentGuardianView)
router.register('fee', views.FeeView)
router.register('payment', views.PaymentView)
router.register('book', views.BookView)
router.register('librarytransaction', views.LibraryTransactionView)
router.register('studentdetails', views.StudentDetailView)



app_name = 'log'

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()