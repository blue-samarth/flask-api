# User Management API

A comprehensive RESTful API for robust user management built with Flask and MongoDB, emphasizing security, scalability, and developer experience.

## 📋 Overview

This application delivers a complete suite of CRUD operations for sophisticated user data management. The architecture follows a layered approach, separating concerns between routing, business logic, data access, and persistence. This design ensures maintainability and allows each component to evolve independently while maintaining system integrity.

The system flow operates as follows:
1. Client requests are received by API endpoints.
2. Requests undergo validation through Pydantic models.
3. Valid requests are processed by the Data Access Object (DAO).
4. The DAO interacts with MongoDB for persistence.
5. Responses are formatted and returned with appropriate status codes.

Every operation is wrapped in comprehensive error handling to provide consistent, informative feedback to API consumers.

## ✨ Features

**User Management Capabilities**  
Provides a full spectrum of operations to create, retrieve, update, and delete user records.

**Data Validation & Integrity**  
Utilizes Pydantic to ensure all incoming data meets strict validation rules before processing.

**Enhanced Password Security**  
Enforces password complexity and automatically hashes passwords securely prior to storage.

**MongoDB Integration**  
Seamlessly integrates with MongoDB using PyMongo for efficient, document-oriented data storage.

**RESTful API Architecture**  
Adheres to REST principles with clear resource-based endpoints and proper HTTP methods.

**Comprehensive Error Management**  
Implements consistent error handling across the API for improved troubleshooting and reliability.

## 🛠️ Tech Stack

- **Flask Framework**: Provides the lightweight, modular backbone of the API.
- **Gunicorn WSGI Server**: Handles concurrent requests efficiently using a pre-fork worker model.
- **MongoDB**: Offers flexible, schema-less document storage.
- **PyMongo Driver**: Enables clean, Pythonic interaction with MongoDB.
- **Pydantic Validation**: Ensures robust, type-safe data validation.
- **uv Package Manager**: Accelerates dependency resolution and environment management.

## 🚀 Installation

### Prerequisites

Before installation, ensure your environment meets these requirements:

- **Python 3.8+**
- **MongoDB 4.4+**
- **uv Package Manager** (recommended for enhanced dependency management)

### Setup Process

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/user-management-api.git
   cd user-management-api
   ```

2. **Create and Activate a Virtual Environment Using uv:**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```
   Using uv speeds up dependency resolution and installation.

4. **Configure Environment Variables:**
   Create a `.env` file in the project root with at least the following variables:
   ```
   FLASK_APP=src/server.py
   MONGO_URI="mongodb://mongodb:27017/users"
   ```
   > **Note:** In Docker Compose, use `mongodb://mongodb:27017/users` so the application connects to the MongoDB service by its name.

5. **Verify MongoDB Availability (for local development):**
   ```bash
   mongod --version
   mongod --dbpath /data/db
   ```
   Ensure that MongoDB is running and accessible before starting the API.

## 🔄 Running the Application

### Development Environment

For rapid development with auto-reload and debugging enabled:
```bash
uv run flask run --debug --port=5000
```
This command runs Flask in development mode, automatically reloading the app when code changes are detected.

### Production Deployment with Gunicorn

For production, use Gunicorn to serve the application:
```bash
# Option 1: Directly run gunicorn (ensure gunicorn is in your .venv/bin)
gunicorn -w 4 -b 0.0.0.0:8000 src.server:app

# Option 2: Use uv run for automatic environment synchronization
uv run gunicorn -w 4 -b 0.0.0.0:8000 src.server:app
```
Adjust the worker count (`-w 4`) based on your server’s CPU capabilities.

## 🚢 Docker Compose Deployment

This project includes a Docker Compose configuration to run the API alongside a MongoDB instance.

### Docker Compose File

Below is an example **docker-compose.yml**:

```yaml
version: '3.8'
services:
  user-api:
    image: user-api
    container_name: user-api
    pull_policy: never
    build:
      context: .
      dockerfile: Dockerfile
      target: runtime
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - mongodb

  mongodb:
    image: mongo
    container_name: user-api-mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongodb-data:/data/db

volumes:
  mongodb-data:
```

### Steps to Run

1. **Build and Start the Services:**
   ```bash
   docker compose up --build -d
   ```

2. **Check Container Status:**
   ```bash
   docker compose ps
   ```

3. **View Logs:**
   ```bash
   docker compose logs -f
   ```

4. **Access the API:**
   Open a browser or use curl to test the endpoint:
   ```bash
   curl http://localhost:8000/ping
   ```
   Ensure your API defines a `/ping` endpoint for health checks.

5. **Stop the Services:**
   ```bash
   docker compose down
   ```

## 📡 API Endpoints

### User Operations

| Method | Endpoint      | Description                     | Request Body             | Response                          | Status Codes  |
|--------|---------------|---------------------------------|--------------------------|-----------------------------------|---------------|
| POST   | /user         | Create a new user account       | User object (JSON)       | Created user with generated ID    | 201, 400      |
| GET    | /user         | Retrieve all users              | None                     | Array of user objects             | 200, 500      |
| GET    | /user/{id}    | Retrieve a user by ID           | None                     | Single user object                | 200, 404      |
| PUT    | /user/{id}    | Update an existing user         | Updated user object      | Updated user object               | 200, 400, 404 |
| DELETE | /user/{id}    | Delete a user                   | None                     | No content                        | 204, 404      |

### Example: Creating a New User

```bash
curl -X POST http://127.0.0.1:8000/user \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe", 
    "email": "john.doe@example.com", 
    "password": "Password@123"
  }'
```

Successful responses follow a standardized envelope with `data`, `message`, and `status_code`.

## 📁 Project Structure

```
user-management-api/
├── src/                          # Source code
│   ├── models/                   # Data models and validation (Pydantic)
│   ├── repositories/             # MongoDB data access layer
│   ├── utils/                    # Utility modules (error handling, password management)
│   ├── server.py                 # Application entry point and configuration
│   └── __init__.py               # Package initialization
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   └── integration/              # Integration tests
├── .env                          # Environment variables
├── README.md                     # Project documentation (this file)
└── requirements.txt              # Dependency specifications
```

## 🐞 Error Handling Strategy

The API uses custom exception classes to capture errors consistently. Each route wraps its logic in try-except blocks that convert exceptions into standardized JSON error responses with appropriate HTTP status codes.

## 🧪 Testing

Run your tests with:
```bash
uv run pytest
```
For coverage reports:
```bash
uv run pytest --cov=src --cov-report=html
```

## 🧠 Development Guidelines

- **Code Style:** Follow PEP 8 guidelines.
- **Documentation:** Document functions and classes with clear docstrings.
- **Error Handling:** Use custom exceptions and include detailed error messages.
- **Type Hints:** Use type annotations for clarity and to support static type checking.
- **Testing:** Write tests for new features and ensure existing tests pass.

## 🔄 Advanced uv Usage

Leverage `uv` to manage environments and dependencies efficiently:

- **Create Virtual Environment:**
  ```bash
  uv venv .venv --python=3.9
  ```
- **Install Dependencies:**
  ```bash
  uv pip install -r requirements.txt
  ```
- **Run Application:**
  ```bash
  uv run flask run --debug --port=5000
  ```
- **Run Gunicorn in Production:**
  ```bash
  uv run gunicorn -w 4 -b 0.0.0.0:8000 src.server:app
  ```

## 🔐 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes with clear messages.
4. Push to your fork and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
