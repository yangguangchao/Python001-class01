from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments

def index(request):
    condtions = {'rating_star__gt': 3}
    shorts = Comments.objects.all()
    query_results = shorts.filter(**condtions)
    return render(request, 'index.html', locals())