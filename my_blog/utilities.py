from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import *


class ObjectDetailMixin:
    """unites common in Post and Tag classes"""
    model = None
    template = None

    def get(self, request, slug):
        """Create page with post content"""
        # post = Post.objects.get(slug__iexact=slug)
        objects = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): objects})


class ObjectCreateMixin:
    """Common for Post and Tag creations staff"""
    form_model = None
    template = None
    model = None

    def get(self, request):
        """form for creating form"""
        form = self.form_model
        return render(request, self.template, context={'form': form})

    def post(self, request):
        """read data from forms"""
        bound_form = self.form_model(request.POST, request.FILES)

        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.author = request.user
            new_obj.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    form = None
    template = None

    """modification existing tags"""
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, request.FILES, instance=obj)
        print(bound_form.is_valid, request.POST, request.FILES)
        if bound_form.is_valid():
            renew_obj = bound_form.save()
            return redirect(renew_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))