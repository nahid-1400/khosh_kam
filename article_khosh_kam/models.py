from django.db import models
from account_khosh_kam.models import User
from malile_khosh_kam.models import CateGory, IPAddress
from django.utils import timezone
class Article(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    STATUS_CHOICES = (
        ('d', ' پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'در حال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='عنوان در url')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='article_image', verbose_name='تصویر')
    published_time = models.DateTimeField(default=timezone.now(), verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(CateGory, blank=True, null=True, verbose_name='دسته بندی', related_name='post_category')
    like_user = models.ManyToManyField(User, blank=True, null=True, verbose_name='پسندها')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'