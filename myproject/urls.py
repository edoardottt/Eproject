
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    url(r'^Eproject/', include('Eproject.urls')),
    path('admin/', admin.site.urls),
]
