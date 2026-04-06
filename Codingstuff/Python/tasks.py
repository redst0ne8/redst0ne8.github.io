import json

def welcome():
    print("Welcome to the Python tasks scheduler!")
    print("Choose what option you want for your scheduler:")
    print("1. Add a new task")
    print("2. View all/specific days tasks")
    print("3. Modify a task")
    print("4. Exit")
    welcome_choice = input("Enter your choice (1-4): ")
    return welcome_choice

def add_task(name, date, time):
    file_path = 'tasks.json'

    with open(file_path, 'r') as file:
        data = json.load(file)

    new_task = {f"task{counter}": {"name": name, "date": date, "time": time}}
    data.update(new_task)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return new_task

def main():
    exiting = False
    while not exiting:
        welcome_choice = int(welcome())
        if welcome_choice == 1:
            name = input("What is the name of the task to add? ")
            date = input("What is the date of the task? ")
            time = input("What is the time of the task? ")
            add_task(name, date, time)
        elif welcome_choice == 2:
            # View tasks logic
            pass
        elif welcome_choice == 3:
            # Modify task logic
            pass
        elif welcome_choice == 4:
            print("Exiting the scheduler. Goodbye!")
            exiting = True

if __name__ == "__main__":
    main()