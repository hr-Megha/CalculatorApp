

tasks = []

def add_Tasks(task):
    tasks.append(task)


def show_Tasks():
    for task in tasks:
        print(task)

while True:
    choice=input("1=Add, 2-Show, 3-Exit")
    task=input("Enter the Task:")

    if choice=="1":
        add_Tasks(task)
    elif choice=="2":
        show_Tasks()
    elif choice=="3":
        break








