from django.db import models
from django.utils import timezone


class CateGoryManager(models.Manager):
    def category_status(self, slug):
        return self.filter(status=True, slug=slug)

    def category_active(self):
        return self.filter(status=True)

class CateGory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='عنوان دسته بندی در url')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='children', verbose_name='والد')
    status = models.BooleanField(default=True, verbose_name='این دسته بندی  نمایش داده شوند؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    image = models.ImageField(upload_to='category', default='category/defualt.jpg', verbose_name='تصویر دسته بندی')

    objects = CateGoryManager()
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

class IPAddress(models.Model):
    ip = models.GenericIPAddressField(verbose_name='آی پی آدرس')

    class Meta:
        verbose_name = 'آی پی آدرس کاربر'
        verbose_name_plural = 'آی پی آدرس کاربران'

    def __str__(self):
        return self.ip


STATUS_CHOICES = (
    ('d', ' پیش نویس'),
    ('p', 'منتشر شده'),
    ('i', 'در حال بررسی'),
    ('b', 'برگشت داده شده'),
)

class MalileManager(models.Manager):
    def active_malile(self):
        return self.filter(status='p', existing=True)

    def published_malile(self):
        return self.filter(status='p')




class Malile(models.Model):
    title = models.CharField(max_length=500, default=None, verbose_name='عنوان')
    image = models.ImageField(upload_to='image_malile', verbose_name='تصویر')
    descriptions = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(max_length=1000000, default=0, verbose_name='قیمت')
    category = models.ManyToManyField(CateGory, related_name='malile_category', verbose_name='دسته بندی')
    height = models.IntegerField(default=0, verbose_name='طول')
    width = models.IntegerField(default=0, verbose_name='عرض')
    weight = models.IntegerField(default=0, verbose_name='وزن')
    discount = models.IntegerField(default=0, verbose_name='تخفیف')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    published_time = models.DateTimeField(default=timezone.now(), verbose_name='زمان انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    is_special = models.BooleanField(default=False, verbose_name='محصول ویژه')
    existing = models.BooleanField(default=True, verbose_name='موجود')
    hits = models.ManyToManyField(IPAddress, blank=True,null=True, related_name='hits', verbose_name='بازدیدها')
    
    objects = MalileManager()

    class Meta:
        verbose_name = 'ملیله'
        verbose_name_plural = 'ملیله ها'

    def __str__(self):
        return self.title

    def get_discounted_malile_price(self):
        result = int(self.price - (self.price * (self.discount / 100)))
        round_result = round(result, 3)
        return round_result

class MalileHit(models.Model):
    malile = models.ForeignKey(Malile, default=None, verbose_name='ملیله', on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, verbose_name='آی پی آدرس', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'بازدید ملیله'
        verbose_name_plural = 'بازدید ملیله ها'

    def __str__(self):
        return self.malile


class MalileGallery(models.Model):
    malile = models.ForeignKey(Malile, default=None, verbose_name='ملیله', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='malile/{malile.title}/image_malile', verbose_name='تصویر')

    class Meta:
        verbose_name = 'گالری تصاویر ملیله'
        verbose_name_plural = 'گالری تصاویر ملیله ها'

    def __str__(self):
        return f'{self.malile.title}-{self.id}'

