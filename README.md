# E-Commerce API

This project is an API for managing products in an e-commerce application. It is built using Django and Django REST Framework (DRF). The API allows users to perform CRUD (Create, Read, Update, Delete) operations on products.

## Features

- Fetch a list of products
- Create a new product
- Update an existing product
- Delete a product

## Prerequisites

- Python 3.9 or later
- Django 4.x
- Django REST Framework
- Postman (or a similar tool for testing API endpoints)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Endpoint                | Method | Description              |
|-------------------------|--------|--------------------------|
| `/api/products/`        | GET    | Fetch all products       |
| `/api/products/<id>/`   | GET    | Fetch a single product   |
| `/api/products/`        | POST   | Create a new product     |
| `/api/products/<id>/`   | PUT    | Update a product         |
| `/api/products/<id>/`   | DELETE | Delete a product         |

## Testing

You can test the endpoints using Postman or curl. Below are examples of some requests:

### Fetch All Products
```bash
GET http://127.0.0.1:8000/api/products/
```

### Create a New Product
```bash
POST http://127.0.0.1:8000/api/products/
Content-Type: application/json
{
    "name": "Product Name",
    "price": 99.99,
    "description": "Product Description",
    "stock": 10
}
```

### Update a Product
```bash
PUT http://127.0.0.1:8000/api/products/<id>/
Content-Type: application/json
{
    "name": "Updated Name",
    "price": 79.99,
    "description": "Updated Description",
    "stock": 5
}
```

### Delete a Product
```bash
DELETE http://127.0.0.1:8000/api/products/<id>/
```

## Directory Structure

```
Ecommerce-API/
|-- env/
|-- products/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- views.py
|-- db.sqlite3
|-- manage.py
|-- README.md
|-- requirements.txt
```

## Contribution

If you want to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

[MIT License](LICENSE)
