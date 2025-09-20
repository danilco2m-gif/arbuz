class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "da" if self.done else "ne"
        return f"{self.title} (до {self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, deadline):
        self.tasks.append(Task(title, deadline))

    def done(self, index):
        if 0 <= index < len(self.tasks):

           self.tasks[index].mark_done()
    def show(self):
        if not self.tasks:
            print("no zadacha")
        else:
            for i, t in enumerate(self.tasks, 1):
                print(f"{i}. {t}")


manager = TaskManager()

while True:
    cmd = input("\n[a]dobavit [s]pokazatu [d]gotovo: ").strip().lower()

    if cmd == "a":
        title = input("imya: ")
        deadline = input("srok: ")
        manager.add(title, deadline)
    elif cmd == "s":
        pass  
    elif cmd == "d":
        num = int(input("zadachka?: ")) - 1
        manager.done(num)
    else:
        print("i chto eto?")

  
    print("\ntekushie zadania:")
    manager.show()