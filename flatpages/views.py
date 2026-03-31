# articles/views.py
from django.http import HttpResponse, Http404  # Добавьте Http404
from django.shortcuts import render
from .models import Article

# Первое задание: простой текст
def home(request):
    return render(request, 'templates/static_handler.html')

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Новая функция для отображения отдельной статьи
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")