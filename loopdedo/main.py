"""Loopdedo API."""

from flask import request, Flask
from playhouse.shortcuts import model_to_dict

from loopdedo import dbo

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web",
)


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int) -> dict:
    """Get a single todo item."""
    return model_to_dict(dbo.Todo.get_by_id(todo_id))


@app.route("/todo", methods=["POST"])
def create_todo() -> dict:
    """Create a new todo item."""
    new_todo = dbo.Todo(**request.form)
    new_todo.save()
    return model_to_dict(new_todo)


@app.route("/todo/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id: int) -> dict:
    """Update an existing todo item."""
    todo = dbo.Todo.get_by_id(todo_id)
    todo.description = request.form['description']
    todo.frequency = request.form['frequency']
    todo.last_completed = request.form['last_completed'] if 'last_completed' in request.form else None
    todo.last_delayed = request.form['last_delayed'] if 'last_delayed' in request.form else None
    todo.save()
    return model_to_dict(todo)


@app.route("/todo/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int) -> dict:
    """Delete todo."""
    dbo.Todo.get_by_id(todo_id).delete()
    return {}


@app.route("/todos")
def get_todos() -> list[dict]:
    """Return all todos."""
    return [d for d in dbo.Todo.select().dicts()]


if __name__ == "__main__":
    app.run()
