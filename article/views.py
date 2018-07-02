from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from .forms import ArticleForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    #return HttpResponse("Hello World")
    #return HttpResponse("You are looking at my_args %s" % my_args)
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})

def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.categroy = request.user
            article.date_time = datetime.now()
            article.save()
            return redirect('detail', id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})





