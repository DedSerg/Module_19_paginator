Запросы QuerySet

from task1.models import Buyer, Game

Регистрация покупателей
first_buyer = Buyer.objects.create(name='Максим', balance=100.00, age=24)
second_buyer= Buyer.objects.create(name='Данила', balance=50.00, age=52)
third_buyer = Buyer.objects.create(name='Сергей', balance=150.00, age=16)

Создание игр
game1 = Game.objects.create(title='Скадинавский бой', cost=20.00, size=1.5, description='Игра года', age_limited=False)
game2 = Game.objects.create(title='Каркассон', cost=30.00, size=2.0, description='Проверенно временем', age_limited=True)
game3 = Game.objects.create(title='Бэнг!', cost=40.00, size=3.0, description='Хит продаж', age_limited=False)



first_buyer = Buyer.objects.get(age__lt=18)
second_buyer, third_buyer = Buyer.objects.filter(age__gt=18)

Game.objects.get(id=10).buyer.set((third_buyer, second_buyer, first_buyer))
Game.objects.get(id=11).buyer.set((second_buyer, third_buyer))
Game.objects.get(id=12).buyer.set([third_buyer])
