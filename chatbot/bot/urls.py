from django.urls import path
from .views import chat

app_name = 'bot'  
urlpatterns = [
    path('chat/', chat, name='chat'),
]
