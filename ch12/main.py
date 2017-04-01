import sys
import tasks as t

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
        print("Invalid command\n Use {0}/{1}/{2}".format(ADD,REMOVE,LIST))
        sys.exit(1)

    if command == ADD:
        title = args[2]
        content = args[3]
        t.add_task(title, content)
    elif command == REMOVE:
        task_id = args[2]
        t.remove_task(task_id)
    elif command == LIST: 
        t.list_task()
    else:
        print("invalid command!")


# adding this line executes the main function
# without this line, the code doesn't run.
main()