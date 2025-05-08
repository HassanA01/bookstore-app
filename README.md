# Django Book Catalog App

A simple Django application for managing a book catalog/store.

## Setup Instructions

1. Clone the repository:

```bash
git clone git@github.com:HassanA01/django-app.git
cd bookstore-app
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Go to `http://localhost:8000` in your browser to access the application.

## Development Notes

The commands (`populate_books.py` and `populate_book_tags.py`) was generated using AI to speed up mock data population in the tables once I decided my design and setup the models to speed up the remainder development process.

## Additional Notes

I decided to apply a book store theme to my assessment to further contextualize the web app and to give you a better experiencing using my website!

## Database Design

Below is the database schema design for the application:

![Database Design](database_design.svg)
