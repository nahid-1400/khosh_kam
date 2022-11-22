from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from malile_khosh_kam.models import Malile
from comment_khosh_kam.models import Comment
from comment_khosh_kam.forms import CommentForm


class MalileDetail(DetailView):
    model = Malile
    template_name = 'malile_khosh_kom/malile_detail.html'

    def get_object(self, queryset=None):
        global malile_id
        malile_id = self.kwargs.get('malile_id')
        malile = get_object_or_404(Malile.objects.active_malile(), id=malile_id)
        return malile

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(malile_id=malile_id).distinct()
        context['form'] = CommentForm(self.request.POST or None)
        return context

class AllMalile(ListView):
    model = Malile
    template_name = 'malile_khosh_kom/all_maliles.html'

    def get_queryset(self):
        return Malile.objects.published_malile()
