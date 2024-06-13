# JSON API

## Description
This is a simple API to store and retrieve JSON data without a predefined schema. It supports basic CRUD operations and persists data in an SQLite database.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd Ansys_coding_assignment-main
    
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## API Endpoints

### POST /data
- Description: Accepts a JSON object and stores it in the database.
- Example Request:
    ```bash
   curl -u admin:password -X POST -H "Content-Type: application/json" -d "{\"key\":\"value\"}" http://127.0.0.1:5000/data

    ```

### GET /data/{id}
- Description: Retrieves the JSON object associated with the given ID.
- Example Request:
    ```bash
    curl http://localhost:5000/data/1
    ```

### PUT /data/{id}
- Description: Updates the existing JSON object with the given ID.
- Example Request:
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d "{\"new_key\":\"new_value\"}" http://localhost:5000/data/1
    ```

### DELETE /data/{id}
- Description: Deletes the JSON object with the given ID.
- Example Request:
    ```bash
    curl -X DELETE http://localhost:5000/data/1
    ```

## Running Tests

1. Ensure the virtual environment is activated.
2. Run the tests:
    ```bash
    python -m unittest discover -s test_api
    ```

## Assumptions

- The application is designed to run on Linux Ubuntu.
- No authentication is implemented in the basic version, but it can be added as needed.
