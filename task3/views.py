from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def task3_view_platform(request):
    return render(request, 'fourth_task/platform.html')
def task3_view_games(request):
    return render(request, 'fourth_task/games.html')
def task3_view_cart(request):
    return render(request, 'fourth_task/cart.html')