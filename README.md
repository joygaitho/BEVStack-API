Project Idea

Project name: BEVStack API
Description:
BEVStack API is a RESTful backend service for managing drinks in a bar or café. It will handle drink listings, categories, pricing, availability, inventory, and orders. The API is designed to be consumed by web or mobile frontends.

# Bevstack API

## Overview

Bevstack is a backend RESTful API built using Django and Django REST
Framework. The project provides endpoints for managing drink categories
and drinks, with secure authentication using JWT.

## Features

-   User registration and JWT authentication
-   CRUD operations for Categories and Drinks
-   Role-based permissions (Admin write access)
-   Filtering, search, and ordering support
-   Custom error handling
-   Swagger API documentation
-   Logging configuration

## Tech Stack

-   Django
-   Django REST Framework
-   SimpleJWT (JWT Authentication)
-   drf-yasg (Swagger Documentation)
-   django-filter

## Project Structure

    BEVStack-API/ 
    ├── .venv/                      # Python virtual environment
    ├── drinks_api/                 # Project configuration folder
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py             # Global settings (JWT, DRF, Database)
    │   ├── urls.py                 # Main URL routing
    │   └── wsgi.py
    ├── core/                       # Main application folder
    │   ├── migrations/             # Database migration files
    │   ├── __init__.py
    │   ├── admin.py                # Admin panel configurations
    │   ├── apps.py
    │   ├── exceptions.py           # Base API exception handler
    │   ├── models.py               # Drink and Category models
    │   ├── permissions.py          # IsAdminOrReadOnly logic
    │   ├── serializers.py          # Data validation (Drink & Category Serializers)
    │   ├── tests.py
    │   ├── permissions.py          # custom permissions
    │   ├── urls.py                 # App-specific URL routing
    │   └── views.py                # CRUD, Webhook, and Health Check logic
    ├── db.sqlite3                  # Development database
    ├── manage.py                   # Django management script
    └── README.md                   # Project documentation

## Installation

1.  Clone the repository:

    ``` bash
    git clone <your-repo-url>
    cd BEVStack API
    ```

2.  Create a virtual environment:

    ``` bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Run migrations:

    ``` bash
    python manage.py migrate
    ```

5.  Start the server:

    ``` bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

-   `POST /api/register/`
-   `POST /api/token/`
-   `POST /api/token/refresh/`

### Categories

-   `GET /api/categories/`
-   `POST /api/categories/`
-   `GET /api/categories/{id}/`
-   `PUT /api/categories/{id}/`
-   `DELETE /api/categories/{id}/`

### Drinks

-   `GET /api/drinks/`
-   `POST /api/drinks/`
-   `GET /api/drinks/{id}/`
-   `PUT /api/drinks/{id}/`
-   `DELETE /api/drinks/{id}/`

Supports: - Filtering (`?category=1`) - Search (`?search=coffee`) -
Ordering (`?ordering=price`)

📘 API Documentation
Overview

This project provides a RESTful API built with:

Django

Django REST Framework

JWT Authentication using djangorestframework-simplejwt

Interactive API documentation powered by Swagger via drf-yasg

The API follows REST principles and implements authentication, filtering, ordering, search, and proper HTTP status codes.

🚀 Running the Project Locally
1️⃣ Clone the repository
git clone <your-repo-url>
cd BEVStack-API
2️⃣ Create virtual environment
python -m venv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Apply migrations
python manage.py migrate
5️⃣ Run development server
python manage.py runserver

Server will run at:

http://127.0.0.1:8000/
📄 Interactive API Documentation

After running the server, documentation is available at:

🔹 Swagger UI
http://127.0.0.1:8000/swagger/
🔹 ReDoc
http://127.0.0.1:8000/redoc/

The documentation is automatically generated from serializers and viewsets and complies with the OpenAPI specification.

## Deployed API
https://joygaitho.pythonanywhere.com swagger documentation https://joygaitho.pythonanywhere.com/swagger/

🔐 Authentication (JWT)

This API uses JSON Web Tokens for authentication.

Register User
POST /api/register/

Example request body:

{
  "email": "user@gmail.com",
  "username": "user",
  "password": "userpass123"
}

Response: 201 Created

Login
POST /api/token/

Request:

{
  "email": "user@gmail.com",
  "password": "userpass123"
}

Response:

{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
Access Protected Endpoints

Click Authorize inside Swagger and enter:

Bearer <access_token>

This allows testing protected endpoints directly from the documentation.

📌 Core API Endpoints
Endpoint	Method	Description
/api/categories/	GET	List categories
/api/categories/	POST	Create category (Admin only)
/api/drinks/	GET	List drinks
/api/drinks/	POST	Create drink (Admin only)
/api/drinks/?search=coffee	GET	Search drinks
/api/drinks/?ordering=price	GET	Order drinks
/api/drinks/?category=1	GET	Filter drinks
📊 Features Implemented

Full CRUD operations

JWT Authentication

Role-based permissions

Filtering, search, ordering

Custom error handling

Logging configuration

Interactive API documentation

Proper HTTP status codes

🧠 Design Decisions

ViewSets were used for clean RESTful routing.

select_related() applied for query optimization.

Custom exception handler ensures consistent error structure.

JWT ensures stateless authentication suitable for production APIs.

Documentation auto-generates from code to avoid drift.

✅ Expected HTTP Status Codes

200 OK — Successful GET

201 Created — Resource created

400 Bad Request — Validation error

401 Unauthorized — Missing/invalid token

403 Forbidden — Insufficient permissions

404 Not Found — Resource does not exist

📅 ## Development Timeline
Phase             Focus                  Key Deliverables
Phase 1           Foundations            Initialized Django project; configured models.py for Categories and Drinks.
Phase 2           CRUD Development       Created serializers.py and views.py; established the Browsable API for manual testing.
Phase 3           Filtering & Webhooks   Integrated django-filter for search/ordering; added a CSRF-exempt webhook endpoint for external integrations.
Phase 4           Security & JWT         Implemented SimpleJWT for bearer token authentication and custom IsAdminOrReadOnly permissions.
Phase 5           Polish & Lifecycle     Debugged serializer field errors; implemented token blacklisting for secure logouts.

🔮 ## Future Improvements

-   Advanced validation
-   Deployment configuration
-   Docker setup
-   CI/CD integration

👨‍💻 ## Author
Joy Gaitho

GitHub: @joygaitho
LinkedIn: joy-gaitho

Backend developed as part of a learning project using Django and DRF.
