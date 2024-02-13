from datetime import date

TODO_LIST_PATH = "/home/jahu/_vm-share/src/python/todo-parser/parser-test.md"


def filter_overdue(todo_list: list):
    overdue = []

    today = date.today()

    for todo in todo_list:
        todo_split = todo.split("|")
        due = todo_split[1].split(".")
        due_date = date(int(due[2]), int(due[1]), int(due[0]))
        if due_date < today:
            overdue.append(todo)

    return overdue


def filter_due_today(todo_list: list):
    due_today = []

    today = date.today()

    for todo in todo_list:
        todo_split = todo.split("|")
        due = todo_split[1].split(".")
        due_date = date(int(due[2]), int(due[1]), int(due[0]))
        if due_date == today:
            due_today.append(todo)

    return due_today


def filter_open_todos(todo_list: list):
    open_todos = []

    for todo in todo_list:
        if todo.find("[ ]") != -1:
            open_todos.append(todo)

    return open_todos


def filter_done_todos(todo_list: list):
    done_todos = []

    for todo in todo_list:
        if todo.find("[ ]") == -1:
            done_todos.append(todo)

    return done_todos


def get_todo_list():
    with open(TODO_LIST_PATH, "r", encoding="utf-8") as todo_file:
        todo_l = todo_file.readlines()

    return todo_l


if __name__ == "__main__":
    todo_list = get_todo_list()

    for todo in filter_overdue(todo_list):
        print(f"{todo.strip()}")

    # for todo in filter_due_today(todo_list):
    #     print(f"{todo.strip()}")

    # for todo in filter_open_todos(todo_list):
    #     print(f"{todo.strip()}")

    # for todo in filter_done_todos(todo_list):
    #     print(f"{todo.strip()}")