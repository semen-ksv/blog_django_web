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
    form_model = None
    template = None

    def get(self, request):
        """form for creating form"""
        form = self.form_model
        return render(request, self.template, context={'form': form})

    def post(self, request):
        """read data from forms"""
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})