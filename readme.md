# Quote api

Aptly named django app to fetch inspiring quotes from an other api.



## Installation

### prerequisites
- uv [(installation)](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.10 or higher (lower might work, not tested)
- Django 5.0 or higher (lower might work, not tested)

## Setup
1. Clone the repository
2. Install the requirements
    ```bash
    uv sync
    ```
3. Migrate the database
    ```bash
    python manage.py migrate
    ```
4. Create a superuser and pick a password
    ```bash
   python manage.py createsuperuser --username admin --email admin@example.com
    ```
   
# Running the server
5. Run the server
    ```bash
   python manage.py runserver
    ```
   
# Usage
http://127.0.0.1:8000/quotes/random/ retrieve a random new quote, and store
http://127.0.0.1:8000/quotes/ list of retrieved quotes