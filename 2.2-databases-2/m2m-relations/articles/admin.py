from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data.get('is_main', False):
                main_tags += 1
        if main_tags != 1:
            raise ValidationError('Необходимо выбрать один основной раздел ')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    list_filter = ('published_at',)
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']
    # inlines = [ArticleScopeInline]
