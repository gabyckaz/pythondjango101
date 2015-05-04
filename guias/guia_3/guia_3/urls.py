from django.conf.urls import include, url
from django.contrib import admin
from memoria.views import getDificultades

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dificultades/$', getDificultades),    
]
