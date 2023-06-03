from django.shortcuts import render, redirect
from django.views import generic

from .forms import NewsForm
from .models import News


def index(request):
    data = {
        "title":'Головна сторінка',
        "values": ['guhjk','trgh','856']
    }
    return render(request, 'main/index.html', context=data)

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
    def form_valid(self, form):
        form.save()
        return redirect('index')


