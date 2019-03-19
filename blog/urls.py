from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("<int:article_id>",views.article_page)
]