from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView, ListView
from malile_khosh_kam.models import Malile, CateGory, MalileGallery
from comment_khosh_kam.models import Comment
from comment_khosh_kam.forms import CommentForm
from django.db.models import Q
import sweetify
from order_khosh_kam.models import OrderDetail
from order_khosh_kam.form import OrderForm

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
        context['malile_galley'] = MalileGallery.objects.filter(malile_id=malile_id).distinct()
        context['form'] = CommentForm(self.request.POST or None)
        context['order'] = OrderDetail.objects.filter(order=self.request.user.id, malile_id=malile_id).first()
        context['order_form'] =  OrderForm(self.request.POST or None)

        return context
    
class AllMalile(ListView):
    model = Malile
    paginate_by = 20
    template_name = 'malile_khosh_kom/all_maliles_search_category.html'

    def get_queryset(self):
        request = self.request
        return Malile.objects.published_malile()
    
    def get_context_data(self):
        category = CateGory.objects.category_active()
        context = super().get_context_data()
        context['request'] = self.request
        context['category'] = category
        context['end_malile'] = Malile.objects.published_malile()
        context['old_malile'] = Malile.objects.published_malile().order_by('-id')
        context['cheapest_malile'] = Malile.objects.published_malile().order_by('-price')
        context['expensive_malile'] = Malile.objects.published_malile().order_by('price')

        return context

def filter(request):
    context = {}
    if request.method == 'POST':
        cat_chekck =request.POST.getlist('cat_chekck')
        print(cat_chekck)
        min = request.POST.get('min')
        max = request.POST.get('max')
        print(min, max)
        context['object_list'] = Malile.objects.filter(category__slug__in=cat_chekck, price__range=(int(min), int(max)))

    return render(request, 'malile_khosh_kom/all_maliles_search_category.html', context)


class MalileSearch(ListView):
    paginate_by = 5
    template_name = 'malile_khosh_kom/all_maliles_search_category.html'

    def get_queryset(self):
        global q
        q = self.request.GET.get('q')

        return Malile.objects.filter(Q(title__icontains=q)|Q(descriptions__icontains=q))


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        all_malile = Malile.objects.published_malile()
        context['q'] = q
        context['all_malile'] = all_malile
        context['request'] = self.request
        
        return context

class MalileCateGory(ListView):
    model = CateGory
    paginate_by = 20
    template_name = 'malile_khosh_kom/all_maliles_search_category.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(CateGory.objects.category_status(slug))
        return Malile.objects.filter(category=category).all()

    def get_context_data(self):
        context = super().get_context_data()
        context['category'] = category
        return context

def advanced_filter(request):
    category = CateGory.objects.category_active()
    context = {'category': category}
    return render(request, 'malile_khosh_kom/base/advanced_filter.html', context)

def malile_favorites(request, malile_id):
    malile = get_object_or_404(Malile.objects.active_malile(), id=malile_id)
    if not request.user.is_authenticated:
        sweetify.info(request, 'ورود', text='لطفا وارد حساب کاربری خود شوید', persistent='باشه')
    elif malile in request.user.favorits.all():
        request.user.favorits.remove(malile)
        sweetify.success(request, 'موفقیت', text='محصول مورد نظر با موفقیت از لیست علاقه مندی ها حذف شد.', persistent='باشه')
    else:
        request.user.favorits.add(malile)
        sweetify.success(request, 'موفقیت', text='محصول مورد نظر با موفقیت به لیست علاقه مندی ها اضافه شد.', persistent='باشه')
    return redirect(reverse("malile_khosh_kam:malile_detail", args=[malile_id]))
