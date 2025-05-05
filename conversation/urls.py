from django.urls import path
from . import views

app_name = 'conversation'
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/<int:id>', views.new, name='new'),
    path('<int:id>/', views.chat, name='chat'),
]
