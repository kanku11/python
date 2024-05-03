tasks = []

#adding a task
def addTask():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

#list the tasks added
def orderTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")

#delete the completed tasks
def deleteTask():
  orderTasks()
  try:
    taskToDelete = int(input("Enter the # to delete: "))
    if taskToDelete >= 0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  
#loop to run the app
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Order of tasks")
    print("2. Add a new a task")
    print("3. Delete a task")
    print("4. Quit")

#user's choice
    
    choice = input("Enter your choice: ")

    if (choice == "1"):
      orderTasks()
    elif (choice == "2"):
      addTask()
    elif (choice == "3"):
      deleteTask()
    elif (choice == "4"):
      break
    else:
      print("Invalid input. Please try again.")

  print("See you soon!! 👋👋")
