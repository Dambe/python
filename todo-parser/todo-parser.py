TODO_LIST_PATH = "/home/jahu/_vm-share/notes/obsidian/work/_todo/parser-test.md"


def get_todo_list():
    with open(TODO_LIST_PATH, "r", encoding="utf-8") as todo_file:
        todo_l = todo_file.readlines()

    return todo_l


if __name__ == "__main__":
    todo_list = get_todo_list()
    for todo in todo_list:
        print(f"{todo.strip()}")
