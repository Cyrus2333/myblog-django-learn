from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request,"blog/index.html",{"articles": articles})  

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,"blog/article_page.html",{"article":article})

def new_article(request):
    return render(request,"blog/new_article.html")

def publish(request):
    title = request.POST.get("title","没有标题")
    content = request.POST.get("content","没有内容")
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request,"blog/index.html",{"articles": articles})  
