from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import Tag, Post, Comment, Photography

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Photography)


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('title', 'author', 'date_posted', 'get_image')
    list_filter = ('title',)
    search_fields = ('title', 'body',)
    readonly_fields = ('date_posted', 'get_image')
    fields = ('title',
                'slug',
                'author',
                'body',
                'get_image',
                'post_img',
                'date_posted',
                'tags',)

    def get_image(self, obj):
        if obj.post_img:
            return mark_safe(f'<img src={obj.post_img.url} width="50" >')
        return '-'


admin.site.register(Post, PostAdmin)