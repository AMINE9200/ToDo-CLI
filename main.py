from controllers.task_controller import TaskController
from views.task_view import TaskView

def main():
    controller = TaskController()
    view = TaskView()

    while True:
        print("\n=== ToDo List CLI ===")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            title = input("Titre de la tâche : ")
            desc = input("Description (facultative) : ")
            task = controller.add_task(title, desc)
            view.display_message(f"Tâche '{task.title}' ajoutée !")

        elif choix == "2":
            view.display_tasks(controller.list_tasks())

        elif choix == "3":
            try:
                task_id = int(input("ID de la tâche à terminer : "))
                task = controller.mark_task_completed(task_id)
                if task:
                    view.display_message(f"Tâche '{task.title}' marquée comme terminée ")
                else:
                    view.display_message("Tâche introuvable ")
            except ValueError:
                view.display_message("Veuillez entrer un nombre valide.")

        elif choix == "4":
            try:
                task_id = int(input("ID de la tâche à supprimer : "))
                task = controller.delete_task(task_id)
                if task:
                    view.display_message(f"Tâche '{task.title}' supprimée ")
                else:
                    view.display_message("Tâche introuvable ")
            except ValueError:
                view.display_message("Veuillez entrer un nombre valide.")

        elif choix == "5":
            print(" Au revoir !")
            break

        else:
            view.display_message("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
