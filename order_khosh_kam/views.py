from django.shortcuts import render, get_object_or_404
from order_khosh_kam.models import Order,OrderDetail
from django.shortcuts import reverse, redirect
import sweetify
from malile_khosh_kam.models import Malile
from order_khosh_kam.form import OrderForm

def add_order(request, malile_id):
    order_form = OrderForm(request.POST or None)
    if order_form.is_valid():
        malile = get_object_or_404(Malile.objects.active_malile(), id=malile_id)
        count_malie =  order_form.cleaned_data.get('count')
        if request.user.is_authenticated:
            order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
            if order is None:
                Order.objects.create(owner_id=request.user.id, is_paid=False)
            else:
                price= malile.price
                if malile.discount > 0:
                    price = malile.get_discounted_malile_price()
                order.orderdetail_set.create(malile=malile, price=price, count=count_malie)
                sweetify.success(request, 'موفقیت', text='محصول مورد نظر با موفقیت به سبد خرید اضافه شد.', persistent='باشه')
        else:
            sweetify.info(request, 'ورود', text='لطفا وارد حساب کاربری خود شوید', persistent='باشه')
    return redirect(reverse("malile_khosh_kam:malile_detail", args=[malile_id]))

