from django.contrib import admin

from .models import SiteSettings, ReturnSettings, FAQSettings, LawSettings


# Register your models here.

admin.site.register(SiteSettings)
admin.site.register(ReturnSettings)
admin.site.register(FAQSettings)
admin.site.register(LawSettings)
