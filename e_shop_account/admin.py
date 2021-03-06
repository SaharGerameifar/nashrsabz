from django.contrib import admin
from .models import Profile


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['user']

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)

