class ToDo:
    def __init__(self):
        self.tasks = []

    @staticmethod
    def welcome():
        print("Welcome To TODO List")
        print("-------------------------------")

    def menu(self):
        print("1.Create Task")
        print("2.View Task")
        print("3.Update Task")
        print("4.Delete Task")
        print("5.Exit")
        choice = int(input('Choose:'))
        return choice

    def create_task(self):
        try:
            length = int(input("Enter the number of tasks you want to input:"))
            for i in range(1, length+1):
                task = input(f"Enter task {i}:")
                self.tasks.append(task)
            print("-------------------------------")
            print('Tasks Added Successfully.....')
            print("-------------------------------")
        except Exception as e:
            print('Something went wrong')
            print('Error reason: ', e)

    def view_tasks(self):
        if len(self.tasks) == 0:
            print('The List is empty.........')
        else:
            display = int(input(
                '''
                Press 1 if you want to see the Tasks in list
                or 2 if you want to see the Tasks outside the list:
                '''
            ))

            if display == 1:
                print(self.tasks)
            elif display == 2:
                for x, task in enumerate(self.tasks):
                    print(x, ":", task)
            else:
                print("Invalid Number")

    def update_task(self):
        print(self.tasks)
        task = input("Enter the Task you want to Update:")
        if task not in self.tasks:
            print(f"{task} is not in the ToDO List")
        else:
            task_index = self.tasks.index(task)
            self.tasks[task_index] = input("Enter the Updated Task: ")

    def delete_tasks(self):
        del self.tasks
        print('Your ToDo List is now empty.........')


t = ToDo()
ToDo.welcome()
while True:
    result = t.menu()
    if result == 1:
        t.create_task()
    elif result == 2:
        t.view_tasks()
    elif result == 3:
        t.update_task()
    elif result == 4:
        t.delete_tasks()
    elif result == 5:
        break
    else:
        print("Invalid Number")