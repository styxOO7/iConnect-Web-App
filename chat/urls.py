from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('room', views.room, name='room'),
    # path('<str:room>/', views.room, name='room'),
    # path('checkview', views.checkview, name='checkview'),
    path('entry', views.entry, name='entry'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('getUserList/<str:room>/', views.getUserList, name='getUserList'),
    
]


