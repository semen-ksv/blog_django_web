from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="40" height="40">')

    get_image.short_description = 'Profile image'
