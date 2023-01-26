from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from malile_khosh_kam.models import Malile

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='account/user-profile', default=None, blank=True, null=True, verbose_name='تصویر پروفایل')
    favorits = models.ManyToManyField(Malile, blank=True, null=True, related_name='favorits_malile', verbose_name='علاقه مندی ها')







