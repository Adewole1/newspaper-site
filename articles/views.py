# articles/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = "articles/article_edit.html"
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "articles/article_new.html"
    form_class = ArticleForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin ,CreateView):
    model = Comment
    template_name = "articles/comment_new.html"
    form_class = CommentForm
    login_url = 'login'

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        self.object.author = self.request.user
        form.instance.article = article
        self.object.save()
        return super().form_valid(form)
