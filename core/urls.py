from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('pagina-inicial/', views.pagina_inicial, name='pagina_inicial')
]
