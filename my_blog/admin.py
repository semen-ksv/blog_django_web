from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Tag, Post, Comment

admin.site.register(Tag)
admin.site.register(Comment)

# @admin.register(Post)
# class InLineTag(admin.TabularInline):
#     model = Tag
#     extra = 1

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    # fields = (
    #     'title',
    #     'author',
    #     'slug',
    #     'body',
    #     'date_posted',
    #     'tags',
    # )
    # inlines = [InLineTag]
    list_display = ('title', 'author', 'date_posted', 'get_image')
    list_filter = ('title',)
    search_fields = ('title', 'body',)
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'author',
                'body',
                'post_img',
                'date_posted',
                'tags',
            )
            }),
        )
    def get_image(self, obj):
        if obj.post_img:
            return mark_safe(f'<img src={obj.post_img.url} width="40" height="40">')


admin.site.register(Post, PostAdmin)