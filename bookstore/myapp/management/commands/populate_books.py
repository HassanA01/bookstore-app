# I used GenAI for this to speed up this population of tables process for books
from django.core.management.base import BaseCommand # type: ignore
from myapp.models import Book, Category
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with sample books'

    def handle(self, *args, **kwargs):

        books_data = [  
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction", "price": "9.99"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction", "price": "12.99"},
            {"title": "Dune", "author": "Frank Herbert", "category": "Sci-Fi", "price": "14.99"},
            {"title": "Foundation", "author": "Isaac Asimov", "category": "Sci-Fi", "price": "11.99"},
            {"title": "Steve Jobs", "author": "Walter Isaacson", "category": "Biography", "price": "19.99"},
            {"title": "Becoming", "author": "Michelle Obama", "category": "Biography", "price": "24.99"},
            {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "category": "Fantasy", "price": "15.99"},
            {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": "29.99"},
            {"title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy", "price": "16.99"},
            {"title": "1984", "author": "George Orwell", "category": "Fiction", "price": "10.99"},
            {"title": "Brave New World", "author": "Aldous Huxley", "category": "Fiction", "price": "11.99"},
            {"title": "Sapiens", "author": "Yuval Noah Harari", "category": "Non-fiction", "price": "18.99"},
            {"title": "Educated", "author": "Tara Westover", "category": "Non-fiction", "price": "16.99"},
            {"title": "Atomic Habits", "author": "James Clear", "category": "Non-fiction", "price": "15.99"},
            {"title": "The Lean Startup", "author": "Eric Ries", "category": "Non-fiction", "price": "17.99"},
            {"title": "Ready Player One", "author": "Ernest Cline", "category": "Sci-Fi", "price": "13.99"},
            {"title": "The Martian", "author": "Andy Weir", "category": "Sci-Fi", "price": "14.99"},
            {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": "12.99"},
            {"title": "Elon Musk", "author": "Ashlee Vance", "category": "Biography", "price": "20.99"},
            {"title": "The Diary of a Young Girl", "author": "Anne Frank", "category": "Biography", "price": "9.99"},
        ]

        
        for book_data in books_data:
            category = Category.objects.get(name=book_data['category'])
            
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults={
                    'author': book_data['author'],
                    'price': Decimal(book_data['price']),
                    'category': category
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created book "{book.title}"')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Book "{book.title}" already exists')
                )