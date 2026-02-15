from django.urls import path
from . import views

urlpatterns = [
    path('novo-entretenimento/', views.entretenimento_create, name='entretenimento_create'),
    path('', views.entretenimento_list, name='entretenimento_list')
]