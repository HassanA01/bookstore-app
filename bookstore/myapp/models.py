from django.db import models # type: ignore
from django.core.validators import MinValueValidator # type: ignore


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    tags = models.ManyToManyField(Tag, through='BookTag') 

    def __str__(self):
        return self.title

class BookTag(models.Model):
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'tag')

    def __str__(self):
        return f"{self.book.title} - {self.tag.name}"

