from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def task4_view_platform(request):
    # context={'games': ["Atomic Heart", "Cyberpunk 2077"]}
    header = "Главная страница"
    context = {'header': header}
    return render(request, 'fourth_task/platform.html',context)
def task4_view_games(request):
    header = "Игры"
    games = ["WarCraft", "StarCraft", "Doom 2"]
    context = {'games': games, 'header': header }
    return render(request, 'fourth_task/games.html',context)
def task4_view_cart(request):
    header = "Корзина"
    content = "Ваша корзина пуста"
    context = {'header': header,'content': content}

    return render(request, 'fourth_task/cart.html',context)