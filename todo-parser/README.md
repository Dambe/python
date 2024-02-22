# ToDo List Parser

This Python application allows you to parse, modify, and manage todo lists written in Markdown
format. You can easily sort todos based on different criteria such as due date, status
(resolved or still open), overdue status, etc. Additionally, you can mark todos as done or still
open, delete existing todos, and add new ones.

## Features

- **Parsing**: Parse todo lists written in Markdown format.
- **Sorting**: Sort todos based on various criteria like due date, overdue status, resolved status, etc.
- **Modification**: Mark todos as done or still open, delete existing todos, and add new ones.
- **Flexibility**: Works with any Markdown todo list format.
- **Easy Integration**: Can be integrated into other projects or used standalone.
- **Command-line Interface (CLI)**: Provides a user-friendly CLI for interacting with the todo list.

## Usage

1. **Installation**:
   - Clone this repository:

     ```bash
     git clone https://github.com/Dambe/python.git
     ```

2. **Running the Application**:
   - Navigate to the project directory:

     ```bash
     cd todo-parser
     ```

   - Run the application with Python:

     ```bash
     python3 todo-parser.py
     ```

3. **Interacting with the Application**:
   - Once the application is running, follow the prompts to load, modify, and save your todo list.

## Example Todo List Format

Here's an example of how your todo list should be formatted in Markdown:

```markdown
# Template ToDo
- [ ] <Task> | <due_date [dd.mm.yyyy]>
```

You can also refer to the ToDo List `parser-test.md` which is currently used for testing.
