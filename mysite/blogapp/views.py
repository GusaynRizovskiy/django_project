from django.shortcuts import render
from django.views.generic import ListView
from .models import Article


# Create your views here.

class ArticleListView(ListView):
    template_name = 'blogapp/article-list.html'
    model = Article
    context_object_name = 'articles'