from django.urls import path
from . import views

urlpatterns = [
    path('', views.entretenimento_list, name='entretenimento_list'),
    path('novo-entretenimento/', views.entretenimento_create, name='entretenimento_create'),
    path('<int:id_entretenimento>/', views.entretenimento_detail, name="entretenimento_detail"),
    path('delete/<int:id_entretenimento>/', views.entretenimento_delete, name="entretenimento_delete") 
]