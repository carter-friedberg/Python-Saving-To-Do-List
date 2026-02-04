# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
import atexit
from pathlib import Path

tasks = []
completed_tasks = []

def savetasks():
    with open ('Tasks.txt', 'w') as file:
        file.write("Tasks:\n")
        for task in tasks:
            file.write(f'{task}\n')
        file.write("\n\nCompleted Tasks:\n")
        for completed_task in completed_tasks:
            file.write(f'{completed_task}\n')
        file.close()


def main():
    current_dir = Path(os.getcwd())
    if os.path.exists(current_dir/"Tasks.txt"):
        with open(current_dir/"Tasks.txt", "r") as file:
            mode = ""
            for line in file:
                if line.strip() == "Tasks:":
                    mode = "tasks"
                    continue
                if line.strip() == "Completed Tasks:":
                    mode = "completed_tasks"
                    continue
                if line.strip() == "": continue
                if mode == "tasks":
                    tasks.append(line.strip())
                else:
                    completed_tasks.append(line.strip())
        file.close()
    else:
        open(current_dir/"Tasks.txt", "w").close()
    while True:
        print("1. Add new task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. Show tasks")
        print("5. Exit")
        try:
            action = int(input("Input your choice: "))
            if not (0 < action <= 5):
                raise ValueError("Action number too large. Please select a number from 1 to 4!")
            if action == 1: #Creating a new task
                newtask = input("Enter new task: ")
                tasks.append(newtask)
            elif action == 2:
                if len(tasks) == 0: continue
                for task in tasks:
                    print(str((tasks.index(task) + 1)) + ". " + task)
                try:
                    completed_idx = int(input("Enter completed task number: "))
                    if not (0 < completed_idx - 1 <= len(tasks)):
                        raise ValueError(f"Completed task number too large. Please select a number from 1 to {len(tasks)}!")
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Please try again!")
                else:
                    completed_tasks.append(tasks[completed_idx - 1])
                    print("Completed task: " + tasks[completed_idx - 1])
                    tasks.pop(completed_idx - 1)

            elif action == 3: #Removing a task
                if len(tasks) == 0: continue
                for task in tasks:
                    print(str(tasks.index(task) + 1) + ". " + task)
                try:
                    answer = int(input("Enter task number to remove: "))
                    if not (0 <= answer <= len(tasks)):
                        raise ValueError(f"Number must be in range of 1 to {len(tasks)}!")
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Please try again!")
                else:
                    removedtask = tasks[answer - 1]
                    tasks.pop(answer - 1)
                    print("removed task: " + removedtask + "\n")
            elif action == 4: #Viewing the tasks
                print("Tasks:")
                for task in tasks:
                    print(str(tasks.index(task) + 1) + ". " + task)
                print("\nCompleted Tasks:")
                for completed_task in completed_tasks:
                    print(str(completed_tasks.index(completed_task) + 1) + ". " + completed_task + "\n")
                input("Press any key to continue...")
            elif action == 5: #Quitting the program
                savetasks()
                print("Tasks saved!")
                sys.exit(0)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again!")





if __name__ == '__main__':
    atexit.register(savetasks)
    main()
