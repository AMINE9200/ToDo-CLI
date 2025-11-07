# ToDo CLI – Mini API de gestion de tâches

Ce projet est une mini API en ligne de commande (CLI) écrite en Python, permettant de gérer une liste de tâches (ToDo List) en suivant une architecture MVC et les principes de la POO.

---

##  Objectif

L’application permet d’effectuer les opérations suivantes depuis le terminal :

- Ajouter une tâche  
- Lister toutes les tâches  
- Marquer une tâche comme terminée  
- Supprimer une tâche  
- Quitter l’application

---

##  Structure du projet

todo_cli/
│
├── main.py
│
├── models/
│ └── task.py
│
├── controllers/
│ └── task_controller.py
│
└── views/
└── task_view.py
