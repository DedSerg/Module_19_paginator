from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.views.generic import TemplateView
from pyexpat.errors import messages

from .forms import UserRegister
from .models import *


class platform_game(TemplateView):
    template_name = 'platform.html'


class cart_game(TemplateView):
    template_name = 'cart.html'


def menu_game(request):
    # mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    mydict = Game.objects.all().values()
    paginator = Paginator(mydict, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'games.html', {'page_obj': page_obj})

def sign_up_by_html(request):
    users = []
    users1 = Buyer.objects.all().values()
    n_users = len(users1)
    for i in range(n_users):
        users.append(users1[i]['name'])

    info = {}

    if request.method == 'POST':
        user_have = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if password == repeat_password:
            if age >= 18:
                if is_user == False:
                    user_have = True
                else:
                    info['error'] = 'Такой покупатель уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18 лет'
        else:
            info['error'] = 'Пароль не совпадает'

        if user_have:
            message = (f'Добро пожаловать, {username}!')
            Buyer.objects.create(name=username, balance=0, age=age)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            # Проверка существования пользователя
            if Buyer.objects.filter(name=username).exists():
                messages.error(request, 'Такой покупатель уже существует.')
                return render(request, 'registration_page.html', {'form': form})

            if password != repeat_password:
                messages.error(request, 'Пароли не совпадают.')
                return render(request, 'registration_page.html', {'form': form})

            if age < 18:
                messages.error(request, 'Вы должны быть старше 18 лет.')
                return render(request, 'registration_page.html', {'form': form})

            # Если все проверки пройдены, зарегистрировать пользователя
            Buyer.objects.create(name=username, balance=0, age=age)
            messages.success(request, f'Добро пожаловать, {username}!')

            return redirect('home')  # Перенаправление на главную страницу после успешной регистрации

    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form})
