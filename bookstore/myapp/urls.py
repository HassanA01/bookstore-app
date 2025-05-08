from django.urls import path # type: ignore
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
]