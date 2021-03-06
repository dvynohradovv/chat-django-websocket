"""chat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import IndexView, ChatRoomView, LoginView, logout_view, EditChatRoomView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view),

    path('room/', IndexView.as_view(), name="index"),
    # path('create-room/', ChatRoomView.as_view(), name="create-room"),
    path('room/<str:room_name>/edit/', EditChatRoomView.as_view(), name="edit-room"),
    path('room/<str:room_name>/', ChatRoomView.as_view(), name="room"),
]
