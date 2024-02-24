function add_todo(window) {
    let formData = new FormData();

    let dueDate = null;
    if (window.document.getElementById("add-todo-due-date-enabled").checked) {
        dueDate = new Date();
        dueDate.setMonth(window.document.getElementById("add-todo-due-date-month").value);
        dueDate.setDate(window.document.getElementById("add-todo-due-date-day").value);
    }

    formData.append("description", window.document.getElementById("add-todo-description").value);
    formData.append("frequency", window.document.getElementById("add-todo-frequency").value);
    if (dueDate) formData.append("due_date", dueDate);

    fetch(
        "/todo",
        {
            body: formData,
            method: "post",
        })
        .then(data => console.log(data))
        .then(res => console.log(res))
        .catch(error => console.log(error));
}