TODO_LIST_PATH = "/home/jahu/_vm-share/notes/obsidian/work/_todo/parser-test.md"


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
    open_list = filter_open_todos(todo_list)
    done_list = filter_done_todos(todo_list)

    for todo in open_list:
        print(f"{todo.strip()}")

    for todo in done_list:
        print(f"{todo.strip()}")
