from django.urls import path
from . import views

app_name ='blog' 

urlpatterns = [
    path('', views.index),
    path("<int:article_id>",views.article_page,name="article_page")
]