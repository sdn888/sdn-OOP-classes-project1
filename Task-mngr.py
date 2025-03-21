# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# писание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date        # Срок выполнения
        self.completed = False          # Статус выполнения (по умолчанию - не выполнено)

    def mark_as_completed(self):
        self.completed = True            # Отметить задачу как выполненную

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.due_date}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []                   # Список задач

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)       # Добавить новую задачу в список

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()  # Отметить задачу как выполненную
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи:")
        for index, task in enumerate(self.tasks):
            if not task.completed:         # Проверка на статус выполнения
                print(f"{index}. {task}")  # Вывод текущей задачи


# Пример использования
task_manager = TaskManager()
task_manager.add_task("Сделать ДЗ", "2025-03-22")
task_manager.add_task("Перечитать пособие", "2025-03-23")
task_manager.add_task("Сделать уборку", "2023-03-23")

task_manager.show_current_tasks()

# Отметим первую задачу как выполненную
task_manager.mark_task_as_completed(0)

# Выводим текущие задачи снова
task_manager.show_current_tasks()


### Описание кода:
# 1. **Класс `Task`**:
#    - Содержит атрибуты для описания задачи, срока выполнения и статуса.
#    - Метод `mark_as_completed` изменяет статус задачи на выполненную.
#    - Метод `__str__` предоставляет строковое представление задачи для удобного отображения.

# 2. **Класс `TaskManager`**:
#    - Содержит список задач.
#    - Метод `add_task` позволяет добавлять новые задачи.
#    - Метод `mark_task_as_completed` позволяет отметать задачи как выполненные по индексу.
#    - Метод `show_current_tasks` выводит список текущих (не выполненных) задач.

### Пример использования:
# - Создается объект `TaskManager`, добавляются задачи, и отображается список текущих задач. Затем одна задача отмечается как выполненная, и список задач снова отображается.