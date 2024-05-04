from tasklist import TaskList
import check_input

taskList = TaskList()
def main_menu():
  print("-Tasklist-")
  print(f"Tasks to complete:", len(taskList))
  print("1. Display current task")
  print("2. Display all tasks")
  print("3. Mark current task complete")
  print("4. Add new task")
  print("5. Search by date")
  print("6. Save and quit")
  return input("Enter choice: ")

def get_date():
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 2100)
  return f"{month:02d}/{day:02d}/{year}"

def get_time():
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  return f"{hour:02d}:{minute:02d}"



def main():
  while True:
    choice = main_menu()

    if choice == "1":
      current_task = taskList.get_current_task()
      if current_task:
        print("Current task is: ")
        print(current_task)
        print()
      else:
        print("No current task.")
        print()
        
    elif choice == "2":
      print("All tasks:")
      for index, task in enumerate(taskList, start=1):
        print(f"  {index}. {task}")
        index += 1
      print()
        
    elif choice == "3":
      completed_task = taskList.mark_complete()
      if completed_task:
        print("Marking current task as complete:")
        print(completed_task)
        current_task = taskList.get_current_task()
        if current_task:
          print("New current task is: ")
          print(current_task)
          print()
        else:
          print("No current task: ")
          print()
      else:
        print("No tasks to mark complete.")
        print()
        
    elif choice == "4":
      desc = input("Enter task: ")
      print("Enter due date:")
      date = get_date()
      print("Enter time:")
      time = get_time()
      taskList.add_task(desc, date, time)
      print("Tasks to complete:", len(taskList))
      print()
      
    elif choice == "5":
      print("Enter date to search:")
      date = get_date()
      print(f"Tasks due on {date}:")
      found = False
      index = 1
      for task in taskList:
        if task.date == date:
          print(f"  {index}. {task}")
          index += 1
          found = True
      if not found:
        print("No tasks found for this date.")
      print()
        
    elif choice == '6':
      with open("tasklist.txt", "w") as file:
        for task in taskList:
            file.write(repr(task) + "\n")
      print("Saving List...")
      break
    else:
      print("Invalid choice. Please choose again.")
      
main()