from typing import Any, Dict
from django.db.models import Q, QuerySet # type: ignore
from django.views.generic import ListView # type: ignore
from .models import Book, Category, Tag

class BookListView(ListView):
    """view to show and filter books in the store"""
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        """Get books based on search and filters"""

        books = Book.objects.all()
        
        search = self.request.GET.get('search', '')
        category = self.request.GET.get('category', '')
        tag = self.request.GET.get('tag', '')
        max_price = self.request.GET.get('price_max', '')

        if search:

            books = books.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search)
            )
       
        if category:

            books = books.filter(category__name=category)
        
        if tag:

            books = books.filter(tags__name=tag)
        
        if max_price:

            try:
                books = books.filter(price__lte=float(max_price))
            except ValueError:
                pass
        
        return books
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
        adds categories, tags, and current filter values to the context.
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
            'tags': Tag.objects.all(),
            'search_query': self.request.GET.get('search', ''),
            'category_filter': self.request.GET.get('category', ''),
            'tag_filter': self.request.GET.get('tag', ''),
            'price_max': self.request.GET.get('price_max', ''),
        })
        return context