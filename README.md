# Todo API with Django and Django Rest Framework

A simple Todo API built with Django and Django Rest Framework.

## Table of Contents

- [Todo API with Django and Django Rest Framework](#todo-api-with-django-and-django-rest-framework)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [API Endpoints](#api-endpoints)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Features


- **Todo Endpoints:**
  - Create, read, update, and delete operations for both task and category items.

- **Authentication Endpoints:**
  - User authentication for secure access using JWT (JSON Web Token).

- **Swagger / Redoc Integration:**
  - Integrated Swagger and Redoc for enhanced API documentation.

## Technologies Used

- **Python 3.x:** The programming language used for development.
- **Django:** A high-level Python web framework for building web applications.
- **Django Rest Framework:** A toolkit for building Web APIs in Django.
- **djangorestframework-simplejwt:** A JSON Web Token authentication plugin for Django Rest Framework.
- **drf-yasg:** Swagger generator for Django Rest Framework, used for API documentation.
- **gunicorn:** A WSGI HTTP server for running Django applications in production.
- **psycopg2:** PostgreSQL adapter for Python, enabling Django to interact with PostgreSQL databases.



## API Endpoints


| Endpoint                    | HTTP Method | Path                         |
|-----------------------------|-------------|------------------------------|
| Task List                   | GET         | `/task/`                |
| Create Task                 | POST        | `/task/`                |
| Retrieve Task by ID         | GET         | `/task/{id}/`           |
| Update Task by ID           | PUT         | `/task/{id}/`           |
| Delete Task by ID           | DELETE      | `/task/{id}/`           |
| Category List               | GET         | `/category/`           |
| Create Category             | POST        | `/category/`           |
| Retrieve Category by ID     | GET         | `/category/{id}/`      |
| Update Category by ID       | PUT         | `/category/{id}/`           |
| Delete Category by ID       | DELETE      | `/category/{id}/`           |
| User Signup                 | POST        | `/auth/signup/`          |
| User Login                  | POST        | `/auth/login/`           |
| User Logout                 | POST        | `/auth/logout/`          |
| Access Token (JWT)          | POST        | `/auth/token/`           |
| Refresh Token (JWT)         | POST        | `/auth/token/refresh/`   |
| Verify Token (JWT)          | POST        | `/auth/token/verify/`    |
| Swagger UI                  | -           | `/swagger/`                  |
| Swagger JSON (without UI)   | -           | `/swagger<format>/`          |
| Redoc UI                    | -           | `/redoc/`                    |



## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aliseyedi01/Todo-Api.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Todo-Api
   ```

3. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser for admin access:**

   ```bash
   python manage.py createsuperuser
   ```

3. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

4. **Access the admin panel:**

   - Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - Log in with the superuser credentials created earlier.

## Contributing

Feel free to contribute to the project. Fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

