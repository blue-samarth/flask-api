# User Management API

A comprehensive RESTful API for robust user management built with Flask and MongoDB, emphasizing security, scalability, and developer experience.

## 📋 Overview

This application delivers a complete suite of CRUD operations for sophisticated user data management. The architecture follows a layered approach, separating concerns between routing, business logic, data access, and persistence. This design ensures maintainability and allows each component to evolve independently while maintaining system integrity.

The system flow operates as follows:
1. Client requests are received by API endpoints
2. Requests undergo validation through Pydantic models
3. Valid requests are processed by the Data Access Object (DAO)
4. The DAO interacts with MongoDB for persistence
5. Responses are formatted and returned with appropriate status codes

Every operation is wrapped in comprehensive error handling to provide consistent, informative feedback to API consumers.

## ✨ Features

**User Management Capabilities**
The API provides a full spectrum of user management operations, allowing clients to create new user accounts, retrieve individual or collections of user records, update existing user information, and remove user accounts when necessary. All operations are exposed through intuitive RESTful endpoints.

**Data Validation & Integrity**
Leveraging Pydantic's powerful validation capabilities, every data interaction is thoroughly validated against a defined schema. This includes complex password validation rules, email format verification, and structural consistency checks. This validation layer acts as a gateway, ensuring only well-formed data enters the system.

**Enhanced Password Security**
The system implements a sophisticated password security mechanism that automatically enforces complexity requirements and securely hashes passwords before storage. Password complexity rules ensure robust security by requiring diverse character types, while the hashing mechanism protects credentials even in the event of a data breach.

**MongoDB Integration**
The application seamlessly integrates with MongoDB, providing a flexible document-oriented storage solution. The integration leverages MongoDB's indexing capabilities for optimized query performance and its BSON format for efficient storage of user documents. The PyMongo driver facilitates this integration, providing type-safe interactions with the database.

**RESTful API Architecture**
Following REST principles, the API presents a clean, resource-oriented interface with predictable URL structures and appropriate HTTP method usage. This design facilitates intuitive interaction for client applications and promotes standardization across endpoints.

**Comprehensive Error Management**
The application implements a custom exception handling framework that captures, processes, and formats error responses consistently. This ensures that clients receive informative error messages with appropriate HTTP status codes, facilitating troubleshooting and improving the developer experience.

## 🛠️ Tech Stack

This application leverages a carefully selected technology stack designed for performance, reliability, and developer productivity:

**Flask Framework**
A lightweight yet powerful Python web framework that provides the foundation for the API. Flask's modular design allows for flexibility in architecture while maintaining simplicity. The application uses Flask's Blueprint functionality to organize routes into logical groupings.

**Gunicorn WSGI Server**
A production-grade WSGI HTTP server that handles concurrent requests efficiently. Gunicorn's pre-fork worker model offers robust performance characteristics under load, making it ideal for production deployments.

**MongoDB Database**
A schema-less, document-oriented database that offers flexibility in data modeling. MongoDB's JSON-like document storage aligns perfectly with Python's dictionary structures, enabling natural data transformations between application and persistence layers.

**PyMongo Driver**
The official MongoDB driver for Python, providing a clean, Pythonic interface to MongoDB operations. PyMongo handles connection pooling, cursor management, and BSON serialization/deserialization automatically.

**Pydantic Validation**
A data validation library that leverages Python type annotations to validate and parse complex data structures. Pydantic forms the backbone of the application's data validation strategy, ensuring data integrity at all layers.

## 🚀 Installation

### Prerequisites

Before installation, ensure your environment meets these requirements:

* **Python 3.8+**: The application leverages modern Python features including type annotations, f-strings, and advanced dictionary operations.
* **MongoDB 4.4+**: Required for the document-based storage system with support for transactions and aggregation pipelines.
* **`uv` package manager**: Recommended for improved dependency resolution and installation performance.

### Detailed Setup Process

Follow these steps to set up your development environment:

1. **Clone the repository to your local machine**:
   ```bash
   git clone https://github.com/yourusername/user-management-api.git
   cd user-management-api
   ```

2. **Create an isolated Python environment using `uv`**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
   This creates a dedicated environment for your project dependencies, preventing conflicts with system packages.

3. **Install required dependencies efficiently with `uv`**:
   ```bash
   uv pip install -r requirements.txt
   ```
   The `uv` package manager significantly accelerates dependency resolution and installation compared to traditional pip.

4. **Configure environment variables**:
   Create a `.env` file in the project root directory with the following settings:
   ```
   FLASK_APP=src/server.py
   MONGO_URI="mongodb://127.0.0.1:27017/users"
   ```
   These variables define the application entry point and database connection parameters.

5. **Verify MongoDB availability**:
   ```bash
   # Check MongoDB server version
   mongod --version
   
   # Start MongoDB server with specified data directory
   mongod --dbpath /data/db
   ```
   Ensure MongoDB is running and accepting connections before proceeding.

## 🔄 Running the Application

### Development Environment

For an optimal development experience with automatic code reloading:

```bash
# Run Flask in development mode with debugging enabled
uv run flask run --debug --port=5000
```

This configuration automatically reloads the application when code changes are detected and provides detailed error information when exceptions occur.

### Production Deployment

For production environments, use Gunicorn to handle requests efficiently:

```bash
#!/bin/bash
# Export critical environment variables
export FLASK_APP=src/server.py
export MONGO_URI="mongodb://127.0.0.1:27017/users"

# Launch Gunicorn with 4 worker processes, binding to all interfaces on port 8000
gunicorn -w 4 -b 0.0.0.0:8000 src.server:app
```

For enhanced management using `uv`:

```bash
# Install Gunicorn through uv for version consistency
uv pip install gunicorn

# Execute Gunicorn through uv's environment
uv run gunicorn -w 4 -b 0.0.0.0:8000 src.server:app
```

The worker count (`-w 4`) should be adjusted based on server capabilities, typically 2-4× the number of CPU cores available.

## 📡 API Endpoints

### User Operation Specifications

The API exposes the following endpoints for comprehensive user management:

| Method | Endpoint      | Description                      | Request Body               | Response Format                 | Status Codes |
|--------|---------------|----------------------------------|----------------------------|---------------------------------|--------------|
| POST   | /user         | Creates a new user account       | Complete user object       | Created user with generated ID  | 201, 400     |
| GET    | /user         | Retrieves all registered users   | None                       | Array of user objects           | 200, 500     |
| GET    | /user/{id}    | Retrieves a specific user by ID  | None                       | Single user object              | 200, 404     |
| PUT    | /user/{id}    | Updates an existing user record  | Modified user object       | Updated user object             | 200, 400, 404|
| DELETE | /user/{id}    | Permanently removes a user       | None                       | No content                      | 204, 404     |

### Operational Flow Diagram

The system operates through the following workflow pattern:

```
1. Client Request → 
2. API Controller (Route Handler) →
3. Input Validation →
4. Data Access Object →
5. MongoDB Operations →
6. Response Processing →
7. Client Response
```

At each stage, comprehensive error handling ensures failures are captured and communicated appropriately, preventing cascading errors.

## 📊 Request & Response Formats

### User Object Specification

When creating or updating user records, the API expects a JSON payload with the following structure:

```json
{
  "name": "John Doe",                  // Full name of the user
  "email": "john.doe@example.com",     // Valid email address (unique)
  "password": "SecurePass@123"         // Password meeting complexity requirements
}
```

Additional fields such as `id` or `_id` will be ignored during creation operations but are required for identification during updates.

### Success Response Format

Successful operations return a standardized response envelope containing three key elements:

```json
{
  "data": {
    "_id": "65d21b4667d0d8992e610c85",  // MongoDB ObjectId as string
    "name": "John Doe",                  // User's full name
    "email": "john.doe@example.com"      // User's email address
    // Note: Password is deliberately excluded from responses
  },
  "message": "User created successfully",  // Human-readable operation result
  "status_code": 201                       // HTTP status code
}
```

This format provides both the operation result data and contextual information about the operation outcome.

### Error Response Format

When operations fail, a consistent error format is returned:

```json
{
  "error": "Password must contain at least one special character",  // Specific error description
  "status_code": 400  // Appropriate HTTP status code reflecting the error type
}
```

Common error status codes include:
- `400`: Bad Request (validation failures, malformed input)
- `404`: Not Found (requested resource doesn't exist)
- `500`: Internal Server Error (unexpected system failures)

## 🔐 Password Security Requirements

The system enforces stringent password complexity requirements to ensure account security:

1. **Minimum Length**: All passwords must contain at least 6 characters to provide adequate entropy against brute force attacks.

2. **Character Diversity**: Passwords must include a mix of character types:
   - At least one numeric digit (0-9) 
   - At least one uppercase alphabetic character (A-Z)
   - At least one lowercase alphabetic character (a-z)
   - At least one special character from the set: !@#$%^&*()-+

3. **Automatic Hashing**: Valid passwords are automatically hashed using a secure one-way algorithm before storage, ensuring that plaintext credentials are never persisted.

4. **Hash Detection**: The system intelligently detects if a password is already hashed, preventing double-hashing during update operations.

These requirements balance security needs with usability considerations, creating a robust foundation for account protection.

## 📝 Usage Examples

### Creating a New User Account

To create a new user account, send a POST request to the `/user` endpoint:

```bash
curl -X POST http://127.0.0.1:8000/user \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe", 
    "email": "john.doe@example.com", 
    "password": "Password@123"
  }'
```

Upon successful creation, the server responds with:

```json
{
  "data": {
    "_id": "65d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "message": "User created successfully",
  "status_code": 201
}
```

Note that the password is deliberately excluded from the response for security reasons, and the system has assigned a unique identifier to the new user record.

### Retrieving All User Accounts

To retrieve a list of all registered users, send a GET request to the `/user` endpoint:

```bash
curl -X GET http://127.0.0.1:8000/user
```

The response contains an array of user objects, each following the standard response format:

```json
{
  "data": [
    {
      "_id": "65d21b4667d0d8992e610c85",
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "_id": "65d21c5867d0d8992e610c86",
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ],
  "message": "Users fetched successfully",
  "status_code": 200
}
```

This endpoint is particularly useful for administrative interfaces that need to display all system users.

### Retrieving a Specific User

To retrieve information about a specific user, send a GET request to the `/user/{id}` endpoint, where `{id}` is the MongoDB ObjectId of the user:

```bash
curl -X GET http://127.0.0.1:8000/user/65d21b4667d0d8992e610c85
```

For existing users, the response provides the user details:

```json
{
  "data": {
    "_id": "65d21b4667d0d8992e610c85",
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  "message": "User fetched successfully",
  "status_code": 200
}
```

If the specified user cannot be found, the API returns a 404 error with an appropriate message.

### Updating User Information

To modify an existing user's information, send a PUT request to the `/user/{id}` endpoint:

```bash
curl -X PUT http://127.0.0.1:8000/user/65d21b4667d0d8992e610c85 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith", 
    "email": "john.smith@example.com", 
    "password": "NewPass@123"
  }'
```

Upon successful update, the server responds with the updated user information:

```json
{
  "data": {
    "_id": "65d21b4667d0d8992e610c85",
    "name": "John Smith",
    "email": "john.smith@example.com"
  },
  "message": "User updated successfully",
  "status_code": 200
}
```

The system performs the same validation on updates as it does on creation, ensuring data integrity throughout the user lifecycle.

### Removing a User Account

To permanently delete a user account, send a DELETE request to the `/user/{id}` endpoint:

```bash
curl -X DELETE http://127.0.0.1:8000/user/65d21b4667d0d8992e610c85
```

When the deletion succeeds, the server responds with a 204 No Content status, indicating that the operation completed successfully but no data is returned:

```json
{
  "data": null,
  "message": null,
  "status_code": 204
}
```

This follows REST conventions for DELETE operations, where the resource no longer exists after the operation completes.

## 📁 Project Structure

The application follows a well-organized structure that separates concerns and promotes maintainability:

```
user-management-api/
├── src/                          # Source code directory
│   ├── models/                   # Data models and validation
│   │   └── users.py              # User model with Pydantic validation
│   ├── repositories/             # Data access layer
│   │   └── user_repository.py    # MongoDB interaction logic
│   ├── utils/                    # Utility modules
│   │   ├── exceptions.py         # Custom exception definitions
│   │   ├── responses.py          # Response formatting utilities
│   │   └── handle_passwords.py   # Password hashing and validation
│   ├── server.py                 # Application entry point and configuration
│   └── __init__.py               # Package initialization
├── tests/                        # Test suite directory
│   ├── unit/                     # Unit tests for individual components
│   └── integration/              # Integration tests for API endpoints
├── .env                          # Environment variable definitions
├── README.md                     # Project documentation
└── requirements.txt              # Dependency specifications
```

This structure follows the separation of concerns principle, with clear boundaries between different system components:

1. **Models**: Define data structures and validation rules
2. **Repositories**: Handle data persistence and retrieval
3. **Utils**: Provide cross-cutting functionality
4. **Server**: Configures the application and defines API routes

## 🐞 Error Handling Strategy

The application implements a sophisticated error handling strategy centered around the custom `FlaskException` class. This approach ensures consistent error reporting across all endpoints.

Each API endpoint follows this pattern:

```python
try:
    # Attempt the primary operation
    result = perform_operation(input_data)
    
    # Format successful response
    return make_response(jsonify(APIResponse(
        data=result,
        message="Operation completed successfully",
        status_code=200
    )))
except ValueError as e:
    # Handle validation errors specifically
    raise FlaskException(data=str(e), status_code=400)
except FlaskException as e:
    # Pass through custom exceptions
    raise e
except Exception as e:
    # Catch unexpected errors and convert to FlaskException
    raise FlaskException(str(e), status_code=500)
```

This multi-layered approach:
1. Attempts the operation in a protected context
2. Handles specific known error types individually
3. Passes through already-formatted errors
4. Captures and standardizes unexpected errors

The result is a predictable, consistent error response format regardless of where or how the error originates.

## 🧪 Comprehensive Testing with `uv`

The project supports thorough testing using pytest, with `uv` integration for enhanced performance:

```bash
# Install testing dependencies using uv
uv pip install pytest pytest-cov pytest-mock

# Run the entire test suite
uv run pytest

# Run tests with coverage reporting
uv run pytest --cov=src tests/

# Run specific test categories
uv run pytest tests/unit/
uv run pytest tests/integration/

# Generate HTML coverage report
uv run pytest --cov=src --cov-report=html tests/
```

The test suite should include:

1. **Unit tests** for individual components (models, repositories, utilities)
2. **Integration tests** for API endpoints
3. **Edge case tests** for error handling and validation logic

Test coverage should aim for at least 80% code coverage, with critical components such as validation and error handling having closer to 100% coverage.

## 🧠 Development Guidelines

Follow these development principles to maintain code quality and consistency:

1. **Code Style**: Adhere to PEP 8 style guidelines for all Python code
   - Use 4 spaces for indentation (not tabs)
   - Limit line length to 100 characters
   - Use meaningful variable and function names

2. **Documentation**: Document all code thoroughly
   - Every function and class should have a comprehensive docstring
   - Docstrings should follow the format shown in existing code
   - Complex logic should have inline comments explaining the reasoning

3. **Error Handling**: Follow the established error handling pattern
   - Use specific exception types when possible
   - Always include contextual information in error messages
   - Avoid suppressing errors without logging them

4. **Type Hints**: Use Python type hints consistently
   - All function parameters and return values should be typed
   - Use complex types (List, Dict, Optional, etc.) where appropriate
   - Consider using a type checker like mypy during development

5. **Testing**: Write tests for all new functionality
   - Each new feature should have corresponding test cases
   - Tests should cover both happy paths and error conditions
   - Follow the existing test structure and naming conventions

## 🔍 Advanced `uv` Usage for Development

The `uv` package manager offers several advantages over traditional tooling. Here are detailed examples of how to leverage `uv` effectively during development:

### Efficient Package Management

```bash
# Install a specific package with exact version
uv pip install flask==2.0.1

# Install a package with constraints
uv pip install "pydantic>=2.0.0,<3.0.0"

# Add development dependencies without modifying production requirements
uv pip install pytest pytest-cov --dev

# Update requirements.txt after adding dependencies
uv pip freeze > requirements.txt

# Install your package in development mode for testing
uv pip install -e .
```

### Environment Management

```bash
# Create a new virtual environment with specific Python version
uv venv .venv --python=3.9

# Activate the virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Deactivate when finished
deactivate

# Create a new environment with specific packages pre-installed
uv venv .venv --python=3.9 flask pymongo pydantic
```

### Dependency Analysis and Optimization

```bash
# List all installed packages
uv pip list

# Check for outdated packages
uv pip list --outdated

# Display dependency tree to understand relationships
uv pip list --tree

# Find packages that depend on a specific package
uv pip list --tree | grep pymongo

# Run security audit on dependencies
uv pip audit
```

### Performance Enhancements

```bash
# Perform parallel installation of dependencies
uv pip install -r requirements.txt --parallel

# Use uv to run Python scripts with optimization flags
uv run python -O src/server.py
```

These capabilities make `uv` an invaluable tool for Python development, significantly improving both workflow efficiency and dependency management reliability.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions to this project are welcome and appreciated. To contribute effectively:

1. Fork the repository to your own GitHub account
2. Create a feature branch from the main branch (`git checkout -b feature/your-feature-name`)
3. Implement your changes following the development guidelines
4. Add or update tests to cover your changes
5. Ensure all tests pass by running `uv run pytest`
6. Commit your changes with clear, descriptive commit messages
7. Push your changes to your fork (`git push origin feature/your-feature-name`)
8. Submit a pull request to the main repository

The maintainers will review your contribution and provide feedback or merge it if appropriate.