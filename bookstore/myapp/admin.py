from django.contrib import admin # type: ignore
from .models import Category, Tag, Book, BookTag


admin.site.register(Category) 
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(BookTag) 