# I used GenAI for this to speed up this population of tables process for book tags
from django.core.management.base import BaseCommand # type: ignore
from myapp.models import Book, Tag, BookTag

class Command(BaseCommand):
    help = 'Populate the database with book tags'

    def handle(self, *args, **kwargs):

        tags_data = [
            "Collector's Edition",
            "Illustrated",
            "E-book",
            "Paperback",
            "Hardcover",
            "Young Adult",
            "Classic",
            "Award-Winning",
            "New Arrival",
            "Bestseller"
        ]


        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created tag "{tag_name}"'))


        book_tags = {
            "The Great Gatsby": ["Classic", "Award-Winning", "Hardcover"],
            "To Kill a Mockingbird": ["Classic", "Award-Winning", "Paperback", "Bestseller"],
            "Dune": ["Classic", "Paperback", "Bestseller", "Award-Winning"],
            "Foundation": ["Classic", "Paperback", "Sci-Fi"],
            "Steve Jobs": ["Hardcover", "Bestseller", "New Arrival"],
            "Becoming": ["Hardcover", "Bestseller", "Award-Winning"],
            "Harry Potter and the Philosopher's Stone": ["Young Adult", "Bestseller", "Paperback", "Award-Winning"],
            "The Lord of the Rings": ["Classic", "Collector's Edition", "Illustrated", "Hardcover"],
            "A Game of Thrones": ["Bestseller", "Paperback", "E-book"],
            "1984": ["Classic", "Paperback", "Award-Winning"],
            "Brave New World": ["Classic", "Paperback"],
            "Sapiens": ["Bestseller", "Paperback", "E-book"],
            "Educated": ["Award-Winning", "Paperback", "Bestseller"],
            "Atomic Habits": ["Bestseller", "New Arrival", "E-book"],
            "The Lean Startup": ["Bestseller", "E-book"],
            "Ready Player One": ["Young Adult", "Paperback", "E-book"],
            "The Martian": ["Bestseller", "Paperback", "E-book"],
            "The Hobbit": ["Classic", "Illustrated", "Collector's Edition"],
            "Elon Musk": ["Bestseller", "Hardcover", "New Arrival"],
            "The Diary of a Young Girl": ["Classic", "Paperback", "Award-Winning"]
        }


        for book_title, tags in book_tags.items():
            try:
                book = Book.objects.get(title=book_title)
                for tag_name in tags:
                    tag = Tag.objects.get(name=tag_name)
                    book_tag, created = BookTag.objects.get_or_create(
                        book=book,
                        tag=tag
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Added tag "{tag_name}" to "{book_title}"')
                        )
            except Book.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Book "{book_title}" not found')
                )
            except Tag.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Tag "{tag_name}" not found')
                )