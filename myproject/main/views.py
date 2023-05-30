from django.shortcuts import render
from django.views import generic

from .models import News


# def index(request):
#     return render(request, 'main/index.html')

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    model = News
    context_object_name = 'news_list'

def about(request):
    return render(request, 'main/about.html')

# def create_news(request):
#     return render(request, 'main/about.html')

class CreateNewsView(generic.CreateView):
    template_name = 'main/create_news.html'
    form_class = NewsForm
