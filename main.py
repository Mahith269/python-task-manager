
from storage import load_tasks, save_tasks

# Load existing tasks
tasks = load_tasks()
print("Tasks loaded:", tasks)

# Add a new task
new_task = {
    "id": 1,
    "title": "Complete Milestone 2",
    "completed": False
}

tasks.append(new_task)

# Save updated tasks
save_tasks(tasks)
print("Task saved successfully!")

# Reload to verify persistence
loaded_tasks = load_tasks()
print("Tasks after reloading:", loaded_tasks)
