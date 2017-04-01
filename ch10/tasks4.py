import sys

args = sys.argv

tasks = []

try:
	command = args[1]
except IndexError:
	print("Invalid arguments!")
	sys.exit(1)

if command not in ("add","remove","list"):
    print("Invalid command\n Use add/remove/list")
    sys.exit(1)


if command == "add":
    title = args[2]
    content = args[3]
    task = title + "|" + content
    file = open("tasks.txt", "a")
    file.write(task+"\n")
    file.close()
elif command == "remove":
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    task_id = args[2]
    del tasks[int(task_id)]
elif command == "list": 

    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        print("|-{0}----{1}----{2}----|".format("index", "title", "content"))
        tasks = [task.strip() for task in tasks]
        for i in range(len(tasks)):
            title, content = tasks[i].split('|')
            print("|-{0}--{1}----{2}-|".format(i, title, content))
    file.close()
else:
    print("invalid command!")
