class ValidationError(Exception):
    pass

class Task:
    VALID_STATUSES = ["todo", "in progress", "done"]

    def __init__(self, title, description, status="todo"):
        self.title = title
        self.description = description
        self.set_status(status)


    def set_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValidationError(
                f"'{status}' is not valid. Choose from {self.VALID_STATUSES}"
            )
        self.status = status

    def to_dict(self):
        return{
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

try:
    task = Task("Learn Python", "Finish Day 5", "finished")
except ValidationError as e:
    print("Validation error:", e)