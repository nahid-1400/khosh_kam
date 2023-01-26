from django.shortcuts import render
from article_khosh_kam.models import Article
from django.views.generic import DetailView, ListView

class AllMalile(ListView):
    model = Malile
    paginate_by = 20
    template_name = 'article_khosh_kam/article_list.html'

    def get_queryset(self):
        return Malile.objects.published_malile()
    
    def get_context_data(self):
        context = super().get_context_data()
        context['request'] = self.request
        return context