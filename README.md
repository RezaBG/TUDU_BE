# TUDU Application

## About TUDU

TUDU is a task management application built using FastAPI and SQLAlchemy. It provides users with an intuitive platform to create, update, and manage tasks efficiently. The application integrates a PostgreSQL database, supports RESTful APIs, and ensures seamless task management with a focus on scalability and reliability.

---

## Setup Instructions

### Step 1: Clone the Repository

````bash
git clone https://github.com/your-username/TUDU.git
cd TUDU
```plaintext

### Step 2: Set Up the Virtual Environment

Create and activate the virtual environment:

```bash
python3 -venv .venv
source .venv/bin/activate  # For Linux/Mac
# or
.venv\\Scripts\\activate  # For Windows
```

### Step 3: Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

> Note: Use the virtual environment before installing dependencies to avoid conflicts with global packages.

### Step 4: Configure Environment Variables

Set up the database URLs for both development and testing environments:

Create a .env file in the root directory and add the following lines:

```bash
DATABASE_URL="postgresql+psycopg2://username:password@render-host/tudu_database"
TEST_DATABASE_URL="sqlite:///./test.db"
```

> Note: Ensure .env is included in .gitignore to prevent sensitive information from being committed.

### Step 5: Run Database Migrations

To initialize the database schema and apply migrations:

1. Install Alembic (if not already installed):

   ```bash
   pip install alembic
   ```

2. Apply migrations:

   ```bash
   alembic upgrade head
   ```

### Step 6: Start the Application

Run the application locally with Uvicorn:

```bash
uvicorn src.main:app --reload
```

Access the application at:

```plaintext
http://127.0.0.1:8000
```

To run the application in production:

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker src.main:app
```

### Step 7: Run Tests

To ensure everything is functioning as expected, run the tests using Pytest:

```bash
pytest tests
```

### Resetting the Database

If you need to reset the database during development or testing:

```bash
alembic downgrade base
alembic upgrade head
```

---

## Additional Notes

### Dependency Management

This project uses `requirements.in` and `requirements.txt` for dependency management:

- Add high-level dependencies to `requirements.in`.
- Use `pip-compile requirements.in` to generate `requirements.txt`.

### Debugging Database Connectivity

- Ensure the `DATABASE_URL` is set correctly in .env
- Verify network permissions for accessing the database (e.g., allowlisted IPs).
- Check Render's database dashboard for connection details.

### Debugging SQLite Issues

For testing, SQLite is used as the database. If tables are not persisting as expected, check the teardown logic in tests/conftest.py to ensure tables are not being dropped after tests.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git branch feature/your-feature-name
   ```

3. Make your changes and run tests.
4. Submit a pull request with a clear description of your changes.

---

## Future Plans

- Extend the API to include additional features like task priorities and deadlines.
- Add OAuth-based user authentication.
- Deploy the application using Docker and Kubernetes for scalability.
