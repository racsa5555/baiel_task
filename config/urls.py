from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Dish API",

        description="online backend api for dish",

        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/swagger/',schema_view.with_ui('swagger')),
    path('api/user/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
