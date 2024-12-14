# Authentication Setup in Django

This guide explains how to set up token-based authentication in your Django API using Django Rest Framework (DRF) and JWT (JSON Web Token) authentication.

### **1. Authentication Setup in Django**

To enable token-based authentication for your API, follow these steps:

#### **Step 1: Install Required Packages**

First, install the necessary packages for Django Rest Framework and JWT:

```bash
pip install djangorestframework
pip install djangorestframework-simplejwt
```

#### **Step 2: Update `settings.py`**

In your `settings.py`, configure DRF and the authentication classes:

```python
INSTALLED_APPS += [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

This ensures that authentication is required for all API endpoints by default, and both JWT and token authentication are enabled.

#### **Step 3: Configure Authentication Endpoints**

Next, add the authentication-related endpoints in your `urls.py`:

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Your existing API endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

These endpoints handle obtaining and refreshing JWT tokens.

#### **Step 4: Secure API Endpoints**

To secure existing API endpoints, use the `IsAuthenticated` permission class. Here's an example of how to secure the `get_products` endpoint:

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    # Your product logic here
    return Response({"message": "Authenticated access to products"})
```

This ensures that only authenticated users can access the `get_products` endpoint.

---

### **2. Testing Authentication with Postman**

To test authentication using Postman:

#### **Step 1: Obtain Token**

Send a `POST` request to `/api/token/` with the following request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

You should receive a response with an `access` token and a `refresh` token:

```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

#### **Step 2: Use Token in Requests**

To access protected endpoints, include the `Authorization` header with the `Bearer` token:

```
Authorization: Bearer your_access_token
```

For example, to access the `get_products` endpoint, use this header in the request.

#### **Step 3: Refresh Token**

When the `access` token expires, use the `refresh` token to get a new access token. Send a `POST` request to `/api/token/refresh/` with the following body:

```json
{
  "refresh": "your_refresh_token"
}
```

You will receive a new `access` token.

---

### **3. GitHub Repository**

Ensure that the following files are included in your GitHub repository:

1. **`settings.py`**: Authentication classes configuration.
2. **`urls.py`**: Authentication-related endpoints (`/api/token/` and `/api/token/refresh/`).
3. **Views**: Secure API endpoints with the `IsAuthenticated` permission class.
4. **`AUTHENTICATION.md`**: This markdown file.
