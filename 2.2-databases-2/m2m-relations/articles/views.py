from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    # object_list = Article.objects.order_by(ordering)  # 19 queries, 42ms
    object_list = Article.objects.order_by(ordering).prefetch_related('scopes')  # 17 queries, 41ms
    context = {'object_list': object_list}

    return render(request, template, context)
