from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError
# использовать данные только с словаря clean_data
from django.utils.safestring import mark_safe

from .models import Tag, Post, Comment


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['tag', 'slug']

        # giv butstrap views for forms
        widgets = {
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        """make all slug with lowercase"""
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError(f'Slug {new_slug} may not be "Create"!')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug {new_slug} is already exists!')
        return new_slug


class PostForm(forms.ModelForm):
    post_img = forms.ImageField(label='Select a file', help_text='Jpg, jpeg only')
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ['title', 'body', 'post_img', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        """make all slug with lowercase"""
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError(f'Slug {new_slug} may not be "Create"!')
        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug {new_slug} is already exists!')
        return new_slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
