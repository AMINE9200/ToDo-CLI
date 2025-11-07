class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("Aucune tâche pour le moment.")
        else:
            for task in tasks:
                print(task)

    @staticmethod
    def display_message(message):
        print(message)
