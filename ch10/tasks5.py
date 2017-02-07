import sys

ADD,REMOVE,LIST = "add","remove","list"

# defines the main function
# the name can be anything you want
def main():
    args = sys.argv
    try:
        command = args[1]
    except IndexError:
        print("Invalid arguments!")
        sys.exit(1)

    if command not in (ADD,REMOVE,LIST):
        print("Invalid command\n Use %s/%s/%s"%(ADD,REMOVE,LIST))
        sys.exit(1)

    if command == ADD:
        title = args[2]
        content = args[3]
        add_task(title, content)
    elif command == REMOVE:
        task_id = args[2]
        remove_task(task_id)
    elif command == LIST: 
        list_task()
    else:
        print("invalid command!")

def remove_task(task_id):
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    del tasks[int(task_id)]

def list_task():
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        print("|-%s----%s----%s----|"%("index", "title", "content"))
        tasks = [task.strip() for task in tasks]
        for i in range(len(tasks)):
            title, content = tasks[i].split('|')
            print("|-%d--%s----%s-|" %(i, title, content))
    file.close()

def add_task(title, content):
    task = title + "|" + content
    file = open("tasks.txt", "a")
    file.write(task+"\n")
    file.close()

# adding this line executes the main function
# without this line, the code doesn't run.
main()