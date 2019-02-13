from django.urls import include, path
from newblog import views

urlpatterns = [
    path('', views.index, name='login'),
    path('chat/', views.chat, name='chat1'),
]