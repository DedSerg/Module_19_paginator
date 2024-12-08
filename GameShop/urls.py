"""
URL configuration for GameShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from task1.views import platform_game, cart_game, menu_game
from task1.views import sign_up_by_html, sign_up_by_django



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', platform_game.as_view(), name='home'),  # Главная страница
    path('platform/games/', menu_game, name='menu_game'),
    path('platform/cart/', cart_game.as_view(), name='cart_game'),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),


]
