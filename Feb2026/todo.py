from pathlib import Path

TASKS_FILE = Path(__file__).resolve().parent / "tasks.txt"

def load_tasks():
    if TASKS_FILE.exists():
        return TASKS_FILE.read_text(encoding="utf-8").splitlines()
    return []

def save_tasks(tasks):
    TASKS_FILE.write_text("\n".join(tasks) + ("\n" if tasks else ""), encoding="utf-8")

tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        else:
            print("Empty task not added.")

    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("(no tasks yet)")
        else:
            for t in tasks:
                print("-", t)

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
