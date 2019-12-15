from django import forms
from django.core.exceptions import ValidationError
# использовать данные только с словаря clean_data
from .models import Tag


class TagForm(forms.Form):
    tag = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=50)

    # giv butstrap views for form
    tag.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})

    def clean_slug(self):
        """make all slug with lowercase"""
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create')
        return new_slug

    def save(self):
        """create new slug with method clean_data"""
        new_tag = Tag.objects.create(tag=self.cleaned_data['tag'], slug=self.cleaned_data['slug'])
        return new_tag