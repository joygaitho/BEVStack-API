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

    bevstack/        # Main project configuration
    core/            # Main application containing models, views, serializers

## Installation

1.  Clone the repository:

    ``` bash
    git clone <your-repo-url>
    cd bevstack
    ```

2.  Create a virtual environment:

    ``` bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
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

## Documentation

-   Swagger UI: `/swagger/`
-   ReDoc: `/redoc/`

## Future Improvements

-   Advanced validation
-   Deployment configuration
-   Docker setup
-   CI/CD integration

## Author

Backend developed as part of a learning project using Django and DRF.
