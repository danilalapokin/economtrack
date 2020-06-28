from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def game(request):
    return render(request, 'blog/game.html', {})

def about(request):
    return HttpResponse("<h2>About site</h2>")