from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI app
app = FastAPI()

# Sample database (mock)
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# Pydantic model for validating input data for tasks
class Task(BaseModel):
    task_title: str
    task_desc: Optional[str] = None
    is_finished: Optional[bool] = False

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    # Validate if task exists
    for task in task_db:
        if task['task_id'] == task_id:
            return {"status": "ok", "task": task}
    raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})

@app.post("/tasks")
async def create_task(task: Task):
    # Validate task title is not empty
    if not task.task_title:
        raise HTTPException(status_code=400, detail={"error": "Task title is required"})
    
    # Create new task
    new_task_id = len(task_db) + 1
    new_task = {
        "task_id": new_task_id,
        "task_title": task.task_title,
        "task_desc": task.task_desc,
        "is_finished": task.is_finished
    }
    task_db.append(new_task)
    return {"status": "ok", "task_id": new_task_id}

@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    # Find the task to update
    for task_in_db in task_db:
        if task_in_db['task_id'] == task_id:
            # Update task fields if provided
            if task.task_title is not None:
                task_in_db['task_title'] = task.task_title
            if task.task_desc is not None:
                task_in_db['task_desc'] = task.task_desc
            if task.is_finished is not None:
                task_in_db['is_finished'] = task.is_finished
            return {"status": "ok", "updated_task": task_in_db}
    raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    # Search for the task and delete it
    for task in task_db:
        if task['task_id'] == task_id:
            task_db.remove(task)
            return {"status": "ok"}
    raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})
