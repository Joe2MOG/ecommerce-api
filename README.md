# E-commerce Product API

## Project Overview
The E-commerce Product API is a backend application built with Django and Django REST Framework (DRF). It provides a robust system for managing products on an e-commerce platform, including product management (CRUD), user authentication, and search functionality. This API simulates real-world backend development responsibilities in the e-commerce space, focusing on scalability, performance, and ease of use.


## Features

### Product Management (CRUD)
- *Create, Read, Update, and Delete (CRUD)* products.
- Product attributes:
  - Name
  - Description
  - Price
  - Category
  - Stock Quantity
  - Image URL
  - Created Date
- Validation for required fields:
  - Name
  - Price
  - Stock Quantity
- Future enhancement: Automatically reduce stock quantity when an order is placed.

### User Management (CRUD)
- Implemented CRUD operations for users.
- User attributes:
  - Username (unique)
  - Email (unique)
  - Password
- Only authenticated users can manage products (create, update, delete).

### Product Search
- Search for products by:
  - Name (supports partial matches).
  - Category.
- Pagination for search results to handle large datasets efficiently.

### Product View
- Retrieve a list of products or view individual product details by Product ID.
- Optional filters for:
  - Category
  - Price Range
  - Stock Availability.
- Complete product details include:
  - Name
  - Description
  - Price
  - Category
  - Stock Quantity
  - Image URL


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
---

## Technical Details

### Database
- Django ORM is used to define models and interact with the database.
- Models:
  - Product: Represents products with all necessary attributes.
  - Category: Organizes products into categories (e.g., Electronics, Clothing).
  - User: Represents users managing the products.

### Authentication
- User authentication using Django's built-in authentication system.
- Only authenticated users can perform CRUD operations on products.
- Token-based authentication (JWT) for enhanced security.

### API Design
- Designed with Django REST Framework.
- Adheres to RESTful principles with appropriate HTTP methods (GET, POST, PUT, DELETE).
- Proper error handling with meaningful HTTP status codes (e.g., 404 for not found, 400 for bad request).

### Deployment
- Deployed on [Render](https://render.com).
- Accessible, stable, and secure deployment.

### Pagination and Filtering
- Pagination added to product listing and search endpoints.
- Filters available for:
  - Category
  - Price Range
  - Stock Availability.

---

## Endpoints

### User Endpoints
1. *Register User*  
   - *POST* /api/users/register/  
     *Request Body:*
     json
     {
         "username": "Mary2",
         "email": "mary2@example.com",
         "password": "mary2Password123!"
     }
     
     *Response:*
     json
     {
         "message": "User registered successfully"
     }
     

2. *Login User*  
   - *POST* /api/users/login/  
     *Request Body:*
     json
     {
         "username": "Mary2",
         "password": "mary2Password123!"
     }
     
     *Response:* JWT token for authentication.

3. *User Details*  
   - *GET* /api/users/{id}/

### Product Endpoints
1. *List Products*  
   - *GET* /api/products/list/
   - Supports filters: category, price_range, stock_availability.

2. *Create Product*  
   - *POST* /api/products/create/  
     *Request Body:*
     json
     {
         "name": "Sample Product 2",
         "description": "This is a sample product 2.",
         "price": 20.99,
         "category": "Electronics",
         "stock_quantity": 52,
         "image_url": "http://example.com/image.jpg"
     }
     
     *Response:*
     json
     {
         "id": 1,
         "name": "Sample Product",
         "description": "This is a sample product.",
         "price": 19.99,
         "category": "Electronics",
         "stock_quantity": 10,
         "image_url": "http://example.com/image.jpg",
         "created_date": "2025-01-06T12:00:00Z"
     }
     

3. *Retrieve Product*  
   - *GET* /api/products/{id}/

4. ##### Update a Product*  
- Endpoint: PATCH /api/products/<product_id>/  
- Add the Authorization header: Bearer <access_token>  
- Update a product's price and stock quantity with the following JSON body:  
  json
  {
      "name": "Updated Product",
      "description": "An updated product.",
      "price": 39.99,
      "category": 1,
      "stock_quantity": 40,
      "image_url": "http://example.com/image.jpg"
  }


5. *Delete Product*  
   - *DELETE* /api/products/{id}/

6. *Search Products*  
   - *GET* /api/products/search/  
     *Query Parameters:*
     - name: Partial or full name of the product.
     - category: Category name.

### Category Endpoints
1. *Create Category*  
   - *POST* /api/products/categories/  
     *Request Body:*
     json
     {
         "name": "Electronics"
     }
     

2. *List Categories*  
   - *GET* /api/products/categories/

---

## How to Run Locally

1. Clone the repository:
   bash
   git clone https://github.com/your-username/ecommerce-api.git
   cd ecommerce-api
   

2. Install dependencies:
   bash
   pip install -r requirements.txt
   

3. Apply migrations:
   bash
   python manage.py migrate
   

4. Run the server:
   bash
   python manage.py runserver
   

5. Access the API at: http://127.0.0.1:8000/

---

## Deployed Version
Access the deployed API at: [Deployed API URL](https://ecommerce-api-app-48g3.onrender.com)

---

## Future Enhancements
1. Implement order placement functionality with automatic stock updates.
2. Add user roles for enhanced access control (e.g., Admin, Manager).
3. Extend authentication with social logins.
4. Add more detailed filtering and sorting options for products.

---

## Author
[Joseph Albert](https://github.com/Joe2MOG/ecommerce-api.git)

---

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

