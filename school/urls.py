from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    # path()
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('', include('quiz.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(
        'api/docs/',
         SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs',
         ),
    path('api/log/', include('log.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()