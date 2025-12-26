from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('core/', include('core.urls')),
    path('', RedirectView.as_view(pattern_name='login', permanent=True)),
]
