# import os
# import json
# if os.path.exists("task.json"):
#     with open("task.json", "r") as f:
#         task_list = json.load(f)
#     print(f"Welcome back! Loaded {len(task_list)} tasks.")
# else:
#     task_list = [] 

# # task_list = []
# sub_items = []
# # Input Task + display
# task_name = input("Add Task\n")

# # Item Input + append in sub-items
# while True:
#     items_name = input("Add your items\n")
#     if items_name == "":
#         break

#     item_entry = {
#         "item": items_name,
#         "status": "pending"
#         }
#     sub_items.append(item_entry)
    
# # pending_count = len([item for item in sub_items if item["status"] == "pending"])
# pending_count = 0
# for item in sub_items:
#     if item["status"] == "pending":
#         pending_count += 1

# # 2. Apply your "Red/Green" rules
# if pending_count == 0:
#     print("(G) All Green!")
#     t_status = "Green"
# elif pending_count == 1:
#     print("(R) RED - ALMOST DONE!")
#     t_status = "Red"
# else:
#     print("( ) Pending.")
#     t_status = "Pending"

# Task_Entry = {
#     "Name": task_name,
#     "status": t_status,
#     "Item-Name" : sub_items
# }

# task_list.append(Task_Entry)
# print("...Task List...\n")
# print(task_list)

# with open("tasks.json", "w") as f:
#     # indent=4 makes the file look like a "Box" so you can read it!
#     json.dump(task_list, f, indent=3)

# print("\nTask Saved! Close the program and run it again to see it's still there.")



import os
import json

# 1. LOAD DATA (Only once at the start)
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        task_list = json.load(f)
else:
    task_list = []

sub_items = []

while True:
    print("\n--- TO-DO MANAGER ---")
    print("1. View Tasks")
    print("2. Add New Task")
    print("3. Exit")
    print("4. Delete task")
    
    choice = input("Choose an option: ")

    if choice == "1":
        # CODE TO VIEW AND MARK ITEMS DONE
        for idx, t in enumerate(task_list):
            print(f"[{idx}] {t['Name']} - Status: {t['status']}")
            
    elif choice == "2":
        task_name = input("Add Task\n")
        # YOUR EXISTING ADD-TASK CODE GOES HERE
        while True:
            items_name = input("Add your items\n")
            if items_name == "":
                break

        item_entry = {
            "item": items_name,
            "status": "pending"
        }
        sub_items.append(item_entry)

        pending_count = 0
        for item in sub_items:
            if item["status"] == "pending":
                pending_count += 1

# 2. Apply your "Red/Green" rules
        if pending_count == 0:
            print("(G) All Green!")
            t_status = "Green"
        elif pending_count == 1:
            print("(R) RED - ALMOST DONE!")
            t_status = "Red"
        else:
            print("( ) Pending.")
            t_status = "Pending"

        Task_Entry = {
            "Name": task_name,
            "status": t_status,
            "Item-Name" : sub_items
        }

        task_list.append(Task_Entry)
        print("...Task List...\n")
        print(task_list)
        
    elif choice == "3":
        # SAVE AND QUIT
        with open("tasks.json", "w") as f:
            json.dump(task_list, f, indent=3)
            print("Goodbye!")
            break

    elif choice == "4":
        try:
            index_to_remove = int(input("Enter the number of the task to delete: "))
    
    # Remove it
            removed = task_list.pop(index_to_remove)
            print(f"Successfully deleted: {removed['Name']}")

            # CRITICAL: Save the updated list back to the file!
            with open("tasks.json", "w") as f:
                json.dump(task_list, f, indent=3)

        except IndexError:
            print("Error: That task number doesn't exist!")
        except ValueError:
            print("Error: Please enter a valid number, not text.")