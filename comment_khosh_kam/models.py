from django.db import models
from malile_khosh_kam.models import IPAddress
from malile_khosh_kam.models import Malile
from article_khosh_kam.models import Article
class Comment(models.Model):
    malile = models.ForeignKey(Malile, default=None, on_delete=models.CASCADE, verbose_name='ملیله')
    user_name = models.CharField(max_length=200, verbose_name='نام کاربر')
    text_comment = models.TextField(verbose_name='متن نظر')
    email_comment = models.EmailField(verbose_name='ایمیل کاربر')
    user_ip_address = models.ForeignKey(IPAddress, verbose_name='آی پی آدرس کاربر', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.user_name

