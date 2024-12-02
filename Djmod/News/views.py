from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from django.utils import timezone

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})

def news_create(request):
    if request.method == "POST":
        news = News(
            title=request.POST['title'],
            short_description=request.POST['short_description'],
            content=request.POST['content'],
            username=request.POST['username'],
            publication_date=timezone.now()
        )
        news.save()
        return redirect('news_list')
    return render(request, 'news/news_create.html')

def about(request):
    return render(request, 'news/about.html')