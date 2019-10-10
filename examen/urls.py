
from django.contrib import admin
from django.urls import include, path
from services.urls_services import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('services.urls_services', 'services'), namespace='services')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
