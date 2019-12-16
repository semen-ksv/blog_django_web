from django import forms
from django.core.exceptions import ValidationError
# использовать данные только с словаря clean_data
from .models import Tag, Post


class TagForm(forms.ModelForm):
    # class TagForm(forms.Form):
    # tag = forms.CharField(max_length=50)
    # slug = forms.SlugField(max_length=50)
    #
    # # giv butstrap views for form
    # tag.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

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

    # def save(self):
    #     """create new slug with method clean_data"""
    #     new_tag = Tag.objects.create(tag=self.cleaned_data['tag'], slug=self.cleaned_data['slug'])
    #     return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
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