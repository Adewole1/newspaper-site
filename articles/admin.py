# articles/admin.py

from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline):
    '''Tabular Inline View for Comment'''

    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)