# from django.shortcuts import render
#
# # Create your views here.
# from task1.models import Buyer, Game
#
# # Создание покупателей
# buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=25)  # Старше 18
# buyer2 = Buyer.objects.create(name='Bob', balance=50.00, age=17)    # Младше 18
# buyer3 = Buyer.objects.create(name='Charlie', balance=150.00, age=30)  # Старше 18
#
# # Создание игр
# game1 = Game.objects.create(title='Game 1', cost=20.00, size=1.5, description='Fun game', age_limited=False)  # Без ограничения
# game2 = Game.objects.create(title='Game 2', cost=30.00, size=2.0, description='Exciting game', age_limited=True)  # С ограничением
# game3 = Game.objects.create(title='Game 3', cost=40.00, size=3.0, description='Adventure game', age_limited=False)  # Без ограничения
#
# # Пример вывода данных для проверки
# print(f'Buyers:')
# for buyer in Buyer.objects.all():
#     print(f'- {buyer.name}, Age: {buyer.age}, Balance: {buyer.balance}')
#
# print(f'\nGames:')
# for game in Game.objects.all():
#     print(f'- {game.title}, Cost: {game.cost}, Age Limited: {game.age_limited}')