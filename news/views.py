from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from news.forms import CreateCategoriesForm, CreateNewsForm


def home(request):
    context = {"news": News.objects.all() }
    return render(request, "home.html", context)


def details(request, id):
    new = get_object_or_404(News, id=id)
    context = {"new": new }
    return render(request, "news_details.html", context)


def categories(request):
    form = CreateCategoriesForm()
    if request.method == 'POST':
        form_post = CreateCategoriesForm(request.POST)
        if form_post.is_valid():
            form_post.save() # Estava em duvida e esse video me esclareceu: https://www.youtube.com/watch?v=P55F55GOFAY
            return redirect("home-page")

    context = {"form_categories": form }
    return render(request, "categories_form.html", context)


def news(request):
    form = CreateNewsForm()
    if request.method == 'POST':
        form_post = CreateNewsForm(request.POST, request.FILES) # no recebimento de arquivo colocar segundo parametro
        if form_post.is_valid():
            form_post.save()
            return redirect("home-page")
    context = {"form_news": form }
    return render(request, "news_form.html", context)