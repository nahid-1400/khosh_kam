from django.db import models
from malile_khosh_kam.models import IPAddress
from malile_khosh_kam.models import Malile

class Comment(models.Model):
    malile = models.ForeignKey(Malile, default=None, on_delete=models.CASCADE, verbose_name='ملیله')
    subject_comment = models.CharField(max_length=200, verbose_name='عنوان نظر')
    user_name = models.CharField(max_length=200, verbose_name='نام کاربر')
    text_comment = models.TextField(verbose_name='متن نظر')
    email_comment = models.EmailField(verbose_name='ایمیل کاربر')
    user_ip_address = models.OneToOneField(IPAddress, verbose_name='آی پی آدرس کاربر', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='comment_khosh_kam', verbose_name='والد')


    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.subject_comment
