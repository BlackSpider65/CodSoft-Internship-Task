

import json

def load_tasks(filename):
    try :
        with open(filename,'r') as file:
           return  json.load(file)
    except FileNotFoundError as e :
        return e
    
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks,file)

def main():
    todo_filename = "todo.json"
    tasks = load_tasks(todo_filename)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice:")
        
        if choice == "1":
            title = input("Enter Task title:")
            description = input("Enter Task description:")
            due_date = input("Enter  due date(optinal):") 
            
            tasks.append({
                "title" : title,
                "description" : description,
                "due_date" : due_date,
                "complete":False
            })

            save_tasks(tasks, todo_filename)
            print("Task Added!")

        elif choice == "2" :
            print("\nTasks:")
            for i, task in enumerate(tasks):
                status = "✓" if task["completed"] else " "   
                print(f"{i+1}.[{status}] {task['title']} - {task['description']}")

        elif choice == "3" :
            task_index = int(input("Enter the task number to mark as completed:")) - 1
            if 0 <= task_index <= len(tasks) :
                tasks[task_index]["completed"] = True
                save_tasks(tasks, todo_filename)
                print("Task Mark as completed!")
            else :
                print("Invalid Task Number.")
            
        elif choice == "4" :
            break

if __name__ == "__main__" :
    main()

    

    
        
