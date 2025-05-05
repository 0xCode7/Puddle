from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('details/<int:id>', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),

]
