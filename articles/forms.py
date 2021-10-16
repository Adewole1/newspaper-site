from django import forms
from .models import Comment, Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("title", 'body', )


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)
