class Task:
    _id_counter = 1

    def __init__(self, title, description=""):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "" if self.completed else ""
        return f"[{self.id}] {self.title} - {status}"
