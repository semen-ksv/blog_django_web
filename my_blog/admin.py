from django.contrib import admin
from .models import Tag, Post, Comment

admin.site.register(Tag)
admin.site.register(Comment)

# @admin.register(Post)
# class InLineTag(admin.TabularInline):
#     model = Tag
#     extra = 1

class PostAdmin(admin.ModelAdmin):
    # fields = (
    #     'title',
    #     'author',
    #     'slug',
    #     'body',
    #     'date_posted',
    #     'tags',
    # )
    # inlines = [InLineTag]
    list_display = ('title', 'author', 'date_posted',)
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



admin.site.register(Post, PostAdmin)