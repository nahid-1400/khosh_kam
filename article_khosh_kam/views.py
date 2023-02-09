from django.shortcuts import render
from article_khosh_kam.models import Article
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

class ArticleList(ListView):
    model = Article
    paginate_by = 20
    template_name = 'article_khosh_kam/article_list.html'

    def get_queryset(self):
        return Article.objects.all()

class ArticleDitail(DetailView):    
    model = Article
    template_name = 'article_khosh_kam/article_detail.html'

    def get_object(self, queryset=None):
        global article_id
        article_id = self.kwargs.get('article_id')
        article = get_object_or_404(Article,id=article_id)
        return article

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
    