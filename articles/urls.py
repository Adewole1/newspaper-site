# articles/urls.py

from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    # add_comment_to_post,
    CommentCreateView,
)

urlpatterns = [
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    # path("<pk>/new_comment/", add_comment_to_post, name="comment_new"),
    path("<pk>/new_comment/", CommentCreateView.as_view(), name="comment_new"),
]
