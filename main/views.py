from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView

from .models import Article, Category
from .forms import ArticleForm, CategoryForm, CommentsForm
import pickle as pk


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_category(request, category_id):
    articles = Article.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_tag(request, tag_id):
    articles = Article.objects.filter(tags__id=tag_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def detail_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    article.views += 1
    article.save()

    form = CommentsForm()
    user_has_liked = article.likes.filter(user=request.user.author).exists()
    context = {
        'article': article,
        'form': form,
        'user_has_liked': user_has_liked
    }
    return render(request, 'main/detail_article.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_article.html', context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_category.html', context)


class EditArticleView(UpdateView):
    model = Article
    template_name = 'main/edit_article.html'
    form_class = ArticleForm


def add_comment(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user.author
            comment.save()
            return redirect('detail_article', pk=article.id)



def create_like(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.user.is_authenticated:
        if request.user.author and article.likes.filter(user=request.user.author).exists():
            article.likes.filter(user=request.user.author).delete()
        else:
            article.likes.create(user=request.user.author)
        return redirect('detail_article', pk=article.id)
    else:
        return redirect('login')