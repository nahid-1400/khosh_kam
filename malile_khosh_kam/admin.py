from django.contrib import admin
from malile_khosh_kam.models import Malile, MalileHit, CateGory, IPAddress, MalileGallery

admin.site.register(Malile)
admin.site.register(MalileGallery)
admin.site.register(MalileHit)
admin.site.register(CateGory)
admin.site.register(IPAddress)
