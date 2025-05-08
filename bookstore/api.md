# Bookstore API Documentation

## Book List Endpoint

**URL:** `/`

**Method:** `GET`

**Description:** Returns a list of books that can be filtered using query parameters.

### Query Parameters

| Parameter | Type   | Description                     |
| --------- | ------ | ------------------------------- |
| search    | string | Search books by title or author |
| category  | string | Filter books by category name   |
| tag       | string | Filter books by tag name        |
| price_max | number | Filter books by maximum price   |

### Example Requests

1. Get all books:

```
GET /
```

2. Search for books:

```
GET /?search=harry potter
```

3. Filter by category:

```
GET /?category=Fiction
```

4. Filter by tag:

```
GET /?tag=Bestseller
```

5. Filter by price:

```
GET /?price_max=15.99
```

6. Combine filters:

```
GET /?category=Fiction&tag=Bestseller&price_max=20
```

### Response Format

The response is an HTML page containing a list of books matching the filters. Each book includes:

- Title
- Author
- Category
- Price
- Tags

### Models

#### Book

- title: string
- author: string
- price: decimal
- category: foreign key to Category
- tags: many-to-many with Tag

#### Category

- name: string (unique)

#### Tag

- name: string (unique)

### Example Usage with cURL

```bash
# Get all books
curl http://localhost:8000/

# Search for books
curl http://localhost:8000/?search=harry+potter

# Filter by category
curl http://localhost:8000/?category=Fiction
```
