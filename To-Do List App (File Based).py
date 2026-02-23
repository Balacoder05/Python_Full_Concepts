def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")

def view_tasks():
    with open("tasks.txt", "r") as f:
        print(f.read())

while True:
    choice = input("1.Add 2.View 3.Exit: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    else:
        break