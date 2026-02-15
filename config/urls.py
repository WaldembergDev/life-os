from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from two_factor.urls import urlpatterns as tf_urls
from two_factor.views import LoginView

urlpatterns = [
    path('account/login/', LoginView.as_view(redirect_authenticated_user=True), name='two_factor:login'),
    path('', include(tf_urls)),
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('core/', include('core.urls')),    
    path('entretenimentos/', include('entretenimentos.urls')),
    path('', RedirectView.as_view(pattern_name='pagina_inicial', permanent=False)),
]
