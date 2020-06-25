from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    data = {"header": "Welcome to Economtrack", "message": "It's Liza and Daniel's project", "bgcol": "FF00FF"}
    return render(request, 'blog/post_list.html', context=data)