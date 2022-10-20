tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# Print a list of uncompleted tasks

my_list=[]
for task in tasks:
    if False == task["completed"]:
        my_list.append(task)
    
print(my_list)


# #Print a list of completed tasks

my_list=[]
for task in tasks:
    if True == task["completed"]:
        my_list.append(task)
print(my_list)


# #Print a list of all task descriptions

my_list=[]
for task in tasks:
    my_list.append(task["description"])
print(my_list)



# #Print a list of tasks where time_taken is at least a given time

time = 15
my_list=[]
for task in tasks:
  
    if task["time_taken"] >=15:
        my_list.append(task)
print(my_list)

# time = input("provide needed time")
# my_list=[]
# for task in tasks:
  
#     if task["time_taken"] >=time:
#         my_list.append(task)
# print(my_list)


# #Print any task with a given description

my_list=[]
description="Wash Dishes"
for task in tasks:
    if task["description"] == "Wash Dishes":
        my_list.append(task)
print(my_list)


# # Given a description update that task to mark it as complete.

description="Wash Dishes"
my_list=[]
for task in tasks:
    if task["description"] == "Wash Dishes":
        task["completed"]=True
        my_list.append(task)
print(my_list)


# description=input("task decription")
# my_list=[]
# for task in tasks:
#     if task["description"] == description:
#         task["completed"]=True
#         my_list.append(task)
# print(my_list)


# # Add a task to the list

tasks.append({'description': 'Clean Fridge', 'completed': False, 'time_taken': 'ages'})
print(tasks)

