from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='two_factor:login', permanent=True)),
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('core/', include('core.urls')),    
    path('', include(tf_urls)),
]
