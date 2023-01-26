from django.db import models



class AboutUsModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    active = models.BooleanField(default=False, verbose_name='فعال')



    def save(self, *args, **kwargs):
        if self.active:
            # select all other active items
            qs = type(self).objects.filter(active=True)
            # except self (if self already exists)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            # and deactive them
            qs.update(active=False) 

        super(AboutUsModel, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
        
    def __str__(self):
        return self.title
