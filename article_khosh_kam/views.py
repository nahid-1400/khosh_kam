from django.shortcuts import render
from article_khosh_kam.models import Article
from django.views.generic import DetailView, ListView

class ArticleList(ListView):
    model = Article
    paginate_by = 20
    template_name = 'article_khosh_kam/article_list.html'

    def get_queryset(self):
        return Article.objects.all()
    
