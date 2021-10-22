from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin, DataMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(MyMixin, DataMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    mixin_prop = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class SearchResultsView(ListView):
    model = News
    template_name = 'search_results.html'
    context_object_name = 'news_item'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(
            Q(title__icontains=query) |
            Q(another_title__icontains=query) |
            Q(bibliographic_entry__icontains=query) |
            Q(abstract__icontains=query) |
            Q(abstract_in_another_language__icontains=query) |
            Q(authors__icontains=query)
        )
        return object_list


class NewsByCategory(MyMixin, DataMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(News, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        is_favourite = stuff.is_favourite()
        context['is_favourite'] = is_favourite
        return context


def like_view(request, pk):
    if request.user.is_authenticated:
        news = get_object_or_404(News, id=request.POST.get('news_id'))
        news.likes.add(request.user)
        return HttpResponseRedirect(reverse('view_news', args=[str(pk)]))
    else:
        return HttpResponseRedirect(reverse('login'))


def favourite_news(request, pk):
    if request.user.is_authenticated:
        news = get_object_or_404(News, id=pk)
        if news.favourite.filter(id=request.user.id).exists():
            news.favourite.remove(request.user)
        else:
            news.favourite.add(request.user)
        return HttpResponseRedirect(news.get_absolute_url())
    else:
        return HttpResponseRedirect(reverse('login'))


def news_favourite_list(request):
    user = request.user
    favourite_newss = user.favourite.all()
    context = {
        'favourite_newss': favourite_newss,
    }
    return render(request, 'news/favourite_news.html', context)


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'
