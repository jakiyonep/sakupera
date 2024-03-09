from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.landing.urls')),
    path('fasariona/', include('apps.fasariona.urls')),
]
