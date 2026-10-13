
import json

FILE_NAME = "tasks.json"


def save_tasks(tasks):
    """Save the task list to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
