# FIX: при фильтрации ограничить диапазон вводимых значений
# TODO: добавить приоритет задачи (high, medium, low)
# TODO: добавить дедлайн для задачи
# TODO: сортировка задач по приоритету / дедлайну
# TODO: поиск задачи по названию
# IDEA: показывать задачи с истекающим дедлайном при старте
# IDEA: цветной вывод в терминале (colorama)

# Это MVP для моего первого проекта TODO (v1.5)
import json

# Функции
def find_task(tasks_list, prompt, action, output):
    for task in tasks_list:
        if task['number'] == prompt:
            action(task)
            save_tasks(tasks_list)
            print(output)
            return  True

    print("There is no such task!")
    return False

def input_number(prompt):
    """Проверка ввода числа"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a number!")

def save_tasks(tasks_list):
    """Сохранение задач в json файл"""
    with open('tasks.json', 'w') as file_object:
        json.dump(tasks_list, file_object)

def add_task(tasks_list):
    """Добавление новой задачи и добавление ее в json"""
    if tasks_list:
        max_number = max(task['number'] for task in tasks_list)
    else:
        max_number = 0

    new_task = {'name': input("Enter the task: ").strip(),
                       'number': max_number + 1,
                       'accomplishment': False,
                       'hidden': True,}

    if len(tasks_list) < 3:
        new_task['hidden'] = False

    tasks_list.append(new_task)
    save_tasks(tasks_list)

def mark_task(tasks_list):
    """Пометка выполнения задач и ее сохранение в json"""
    if not tasks_list:
        print("First you need to enter the task!")
        return

    while True:

        task_user_accomplishment = input_number("Enter the number of task: ")

        if find_task(tasks_list, task_user_accomplishment, lambda task: task.update({'accomplishment': True}),
                  "Task marked as accomplished."):
            return # Выходим из функции

def show_tasks(tasks_list, limit=None, filter=None):
    if not tasks_list:
        print("No tasks found.")
        return

    count_completed_tasks = 0
    count = 0
    for task in tasks_list:
        status = "✓" if task['accomplishment'] else "✗"

        # Фильтрация
        if filter == 'done' and not task['accomplishment']:
            continue
        if filter == 'undone' and task['accomplishment']:
            continue

        # Скрытые задачи показываем только если фильтр активен
        if filter is None and task['hidden']:
            continue

        if task['accomplishment']:
            count_completed_tasks += 1

        print(f"{task['number']:>3}. {task['name']:<25} [{status}]")
        count += 1

        if limit is not None and count >= limit:
            break

    total_completed = sum(1 for task in tasks_list if task['accomplishment'])

    if filter == 'done' and count_completed_tasks == 0:
        print("No completed tasks!")

    if filter == 'undone' and count == 0:
        print("All tasks are completed!")

    if filter is None and len(tasks_list) > count:
        print(f"{'':2}...")


    print(f"\n ► Total: {total_completed}/{len(tasks_list)} completed")

def delete_task(tasks_list):
    """Удаление задач и сохранение в json"""
    if not tasks_list:
        print("First you need to enter the task!")
        return

    while True:

        task_user_delete = input_number("Enter the number of task to delete: ")

        if find_task(tasks_list, task_user_delete, lambda task: tasks_list.remove(task), "Task is deleted"):
            return

def edit_task(tasks_list):
    """Редактируем задачу и сохраняем в json"""
    if not tasks_list:
        print("First you need to enter the task!")
        return

    while True:

        task_user_edit = input_number("Enter the number of task, which you want to edit: ")
        if find_task(tasks_list, task_user_edit,
                  lambda task: task.update({'name': input("Enter the new task name: ").strip()}),
                  "Task is edited"):
            return

# флаг для цикла
active = True

# загрузка данных
filename = 'tasks.json'
try:
    with open(filename) as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []
except json.decoder.JSONDecodeError:
    tasks = []
    with open(filename, 'w') as f:
        json.dump(tasks, f)

print(f"\nTODO\n")

# стартовый вывод
show_tasks(tasks, limit=3)

# основной цикл
while active:
    try:
        request = input_number("\nWhat would you like:"
                    "\n1. add a task;"
                    "\n2. mark a task;"
                    "\n3. open filter tasks;" 
                    "\n4. delete a task;" 
                    "\n5. edit a task;"            
                    "\n6. exit;\n"
                    "\nPlease enter a number: ")

        if request == 1:
            add_task(tasks)
        elif request == 2:
            mark_task(tasks)
        elif request == 3:
            for task in tasks:
                task['hidden'] = False

            filter_choice = input_number("Filter:\n1. All\n2. Done\n3. Undone\n: ")
            filter_map = {1: None, 2: 'done', 3: 'undone'}
            show_tasks(tasks, filter=filter_map.get(filter_choice))
        elif request == 4:
            delete_task(tasks)
        elif request == 5:
            edit_task(tasks)
        elif request == 6:
            active = False
            print("\nExit...!")
        else:
            print("Invalid choice.")

    except KeyboardInterrupt:
        print("\nExit...!")
        active = False