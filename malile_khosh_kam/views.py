from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from malile_khosh_kam.models import Malile
from comment_khosh_kam.models import Comment

class MalileDetail(DetailView):
    template_name = 'malile_khosh_kom/malile_detail.html'

    def get_object(self):
        global id
        id = self.kwargs.get('id')
        malile = get_object_or_404(Malile.objects.active_malile(), id=id)
        return malile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(malile_id=id).distinct()
        return context


