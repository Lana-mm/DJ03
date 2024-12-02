from django.urls import path
from .views import news_list, news_detail, news_create, about

urlpatterns = [
    path('', news_list, name='news_list'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('news/create/', news_create, name='news_create'),
    path('about/', about, name='about'),
]