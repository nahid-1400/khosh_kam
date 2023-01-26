from django.db import models
from account_khosh_kam.models import User
from malile_khosh_kam.models import Malile

class Order(models.Model):
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/ نشده')
    payment_data = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

    def __str__(self):
        return self.owner.username


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, default=None, on_delete=models.CASCADE, verbose_name='سبد خرید')
    malile = models.ForeignKey(Malile, default=None, related_name='product_order', on_delete=models.CASCADE, verbose_name=' محصول')
    price = models.IntegerField(default=None, verbose_name='قیمت')
    count = models.IntegerField(default=1, verbose_name='تعداد')

    # def get_sum_product_price(self):
    #     return self.count * self.price

    # def get_discount_price(self):
    #     price_discount = self.product.discount_product * self.price
    #     return price_discount / 100

    # def profit_user(self):
    #     price_discount = self.product.discount_product * self.price
    #     final_price = price_discount / 100
    #     return self.price - final_price

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'جزییات محصول ها'

    def __str__(self):
        return self.malile.title