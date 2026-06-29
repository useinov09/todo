from task_manager import TaskManager

def input_number(prompt):
    """Checking the number input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number!")

def show_tasks(tasks):
    """Show tasks"""
    if not tasks:
        print("No tasks found!")
        return

    for task in tasks:
        print(task)

def initial_output(tasks, limit=None):
    """Show the tasks"""
    if not tasks:
        print("No tasks found!")
        return

    for task in tasks[:limit]:
        print(task)

    completed = sum(1 for task in tasks if task.done)
    print(f"\nTotal: {completed}/{len(tasks)} completed")

manager = TaskManager('tasks.json')

print("\nTODO\n")

initial_output(manager.get_tasks(), limit=3)

# main loop
while True:
    try:
        request = input_number("\nWhat would you like:"
                    "\n1. add a task;"
                    "\n2. mark a task;"
                    "\n3. open filter tasks;" 
                    "\n4. delete a task;"
                    "\n5. delete all tasks;"
                    "\n6. edit a task;"            
                    "\n7. exit;\n"
                    "\nPlease enter a number: ")

        if request == 1:
            manager.add_task(input("\nWhat would you like to add?: "))
        elif request == 2:
             number = manager.mark_done(input_number("\nWhat would you like to mark done?: "))
             if number:
                 print("Task is done!")
             elif not number:
                 print("No tasks found!")
        elif request == 3:
            filter_choice = input_number("Filter:\n1. All\n2. Done\n3. Undone\n: ")
            filter_map = {1: None, 2: 'done', 3: 'undone'}
            if filter_choice in filter_map:
                show_tasks(manager.get_tasks(filter_map[filter_choice]))
            else:
                print("Invalid filter!")
        elif request == 4:
            number = manager.remove_task(input_number("\nWhat would you like to remove?: "))
            if number:
                print("Task is removed!")
            elif not number:
                print("No tasks found!")
        elif request == 5:
            answer = input("\nAre you sure? (y/n): ")
            if answer == 'y':
                remove_check = manager.remove_all_tasks()
                if not remove_check:
                    print("No tasks found!")
                    continue
                print("\nTasks are deleted!")
            else:
                print("\nTasks aren't deleted!")
        elif request == 6:
            number = manager.rename_task(input_number("\nWhat would you like to rename?: "),
                                input("\nEnter a new task name: "))
            if number:
                print("Task is renamed!")
            elif not number:
                print("No tasks found!")
        elif request == 7:
            print("\nExit...!")
            break
        else:
            print("Invalid choice.")

    except KeyboardInterrupt:
        print("\nExit...!")
        break