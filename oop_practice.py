class Task:
    def __init__(self, title, description, status="pending"):
        #init runs automatically when you create an object
        #self means the current object
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "completed"

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Task:{self.title} | Description: {self.description} | Status: {self.status}"

    def __repr__(self):
        return f"Task(title={self.title!r}, description={self.description!r}, status={self.status!r})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (
            self.title == other.title and
            self.description == other.description and
            self.status == other.status
        )

task1 = Task("Study Python", "Learn classes")
task2 = Task("Go Gym", "Train chest", "completed")

task1.mark_complete()

print(task1)
print(repr(task1))


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        return f"My name is {self.name} and my email is {self.email}."

person1 = Person("Raul", "raul@example.com")
print(person1.introduce())

class User(Person):
    def __init__(self, name, email):
        super().__init__(name, email) #calls the parent's class conductor
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return
        for task in self.tasks:
            print(task)

user1 = User("Bob", "bob@gmail.com")

task1 = Task("Study Python", "Learn OOP")
task2 = Task("Go Gym", "Train chest")

user1.add_task(task1)
user1.add_task(task2)

user1.view_tasks()



