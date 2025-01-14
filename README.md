# Django REST Authentication API

This project is a basic authentication API built using Django and Django REST Framework (DRF) that supports user registration, login, and token-based authentication with JSON Web Tokens (JWT).


## Features

- User registration
- User login
- User Profile
- Token-based authentication (JWT)
- Refresh tokens to issue new access tokens

## Requirements

- Python 3.X
- Django 3.X or higher
- Django REST Framework
- MySQL Database (or another Database of your choice)
- PyJWT (for handling tokens)



# Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/amitkumar0198singh/Authentication-API.git
   cd Authentication-API
   ```

2. Create a Virtual Enviornment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Database Settings

   Update the `DATABASE` setting in your `settings.py` file with your MySQL database credentials:
   ```json
   DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "YOUR_DATABASE_NAME",
        "USER": "YOUR_DATABASE_USER",
        "PASSWORD": "YOUR_DATABASE_PASSWORD",
        "HOST": "YOUR_DATABASE_HOST",
        "PORT": "3306",     # Default MySQL Port
    }
   }
   ```

5. Migrate the Database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the Development Server:
   ```bash
   python manage.py runserver
   ```



# Endpoints

1. User Registration

   URL: `/api/register/`

   Method: `POST`

   Request Body:
   ```json
   {
       "name": "new_user_name",
       "username": "new_username",
       "email": "new_user@example.com",
       "password": "password123",
       "confirm_password": "password123"
   }
   ```
   Response Body:
   ```json
   {
       "message": "User created successfully.",
       "tokens": {
           "access": "<access_token>",
           "refresh": "<refresh_token>"
       }
   }
   ```

2. User Login

   URL: `/api/login/`

   Method: `POST`

   Request Body:
   ```json
   {
       "username": "new_username",
       "password": "password123"
   }
   ```
   Response Body:
   ```json
   {
       "message": "Login successful.",
       "tokens": {
           "access": "<access_token>",
           "refresh": "<refresh_token>"
       }
   }
   ```

3. User Profile

   URL: `api/profile/`

   Method: `GET`

   Headers:
   ```

4. Refresh Token

   URL: `/api/refresh-token/`

   Method: `POST`

   Request Body:
   ```json
   {
       "refresh_token": "<refresh_token>"
   }
   ```
   Response Body:
   ```json
   {
       "message": "Token refreshed successfully",
       "new_access_token": "<new_access_token>"
   }
   ```



# Token Management
- `Access Token` : Short-lived token (e.g. 15 minutes). Used to access protected endpoints.
- `Refresh Token` : Long-lived token (e.g. 1 day). Used to obtain a new access token when the old one expires.


## How to Use Access and Refresh Tokens

1. Upon successful registration or login, you will receive both an `access_token` and `refresh_token`.
2. Use the `access_token` in the `Authorization` header of subsequent API requests to access protected resources .
3. If the `access_token` expires, you can use the `refresh_token` to obtain a new `access_token`.

## Example: Accessing User Profie
Make a `GET` request to `/api/profile/` with the `Authorization` header containing the access token:
```http
GET /api/profile/
Authorization: Bearer <access_token>
```
