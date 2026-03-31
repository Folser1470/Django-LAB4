# DjangoLab/urls.py
from django.contrib import admin
from django.urls import path
from flatpages import views  # Измените импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.home, name='hello'),
    path('archive/', views.archive, name='articles'),
    # Добавьте новый URL для отдельной статьи
    path('article/<int:article_id>/', views.get_article, name='get_article'),
]