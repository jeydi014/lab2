# FastAPI Task Manager API

## Description
This is a simple FastAPI-based Task Manager API that allows users to create, retrieve, update, and delete tasks. It uses a mock database and provides endpoints for task management.

## Features
- Retrieve a task by ID
- Create a new task
- Update an existing task
- Delete a task
- Uses Pydantic for data validation

## Installation

### Prerequisites
- Python 3.7+

### Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install fastapi uvicorn pydantic
   ```

## Usage

### Running the API
Start the FastAPI application with Uvicorn:
```sh
uvicorn main:app --reload
```

### API Endpoints

#### Retrieve a Task
**Request:**
```
GET /tasks/{task_id}
```
- `task_id` (int): The ID of the task to retrieve.

**Response:**
```json
{
    "status": "ok",
    "task": {
        "task_id": <task_id>,
        "task_title": "<title>",
        "task_desc": "<description>",
        "is_finished": false
    }
}
```

#### Create a Task
**Request:**
```
POST /tasks
```
**Payload:**
```json
{
    "task_title": "New Task",
    "task_desc": "Task description",
    "is_finished": false
}
```
**Response:**
```json
{
    "status": "ok",
    "task_id": <new_task_id>
}
```

#### Update a Task
**Request:**
```
PATCH /tasks/{task_id}
```
**Payload:**
```json
{
    "task_title": "Updated Task",
    "task_desc": "Updated description",
    "is_finished": true
}
```
**Response:**
```json
{
    "status": "ok",
    "updated_task": {
        "task_id": <task_id>,
        "task_title": "Updated Task",
        "task_desc": "Updated description",
        "is_finished": true
    }
}
```

#### Delete a Task
**Request:**
```
DELETE /tasks/{task_id}
```
**Response:**
```json
{
    "status": "ok"
}
```

### Example Usage
Using `curl`:
```sh
curl -X GET "http://127.0.0.1:8000/tasks/1"
```
Expected Response:
```json
{
    "status": "ok",
    "task": {
        "task_id": 1,
        "task_title": "Laboratory Activity",
        "task_desc": "Create Lab Act 2",
        "is_finished": false
    }
}
```

## License
This project is licensed under the MIT License.

