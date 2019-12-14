from django.shortcuts import render
from django.shortcuts import get_object_or_404

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
