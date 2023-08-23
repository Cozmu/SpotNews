from django.shortcuts import render, get_object_or_404
from news.models import News

def home(request):
    context = {"news": News.objects.all() }
    return render(request, "home.html", context)

def details(request, id):
    new = get_object_or_404(News, id=id)
    context = {"new": new }
    return render(request, "news_details.html", context)