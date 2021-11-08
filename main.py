from os import path
from Interactions import *

def repeat():
    exists_ornot = path.exists("task_saved.json")
    if(exists_ornot==False):
        with open('task_saved.json','w') as temp:
            temp.write('{\"activity\": []}')
            temp.close
    else:pass

    print("Enter the number correspondingly\n1) add task\n2) read_task\n3) delete task\n4) inbetween\n5) Close")
    c=int(input())
    while(c!=5):

        if c==1:
            add_task()
            repeat()
        elif c==2:
            read_task()
            repeat()
        elif c==3:
            delete_task()
            repeat()
        elif c==4:
            inbetween()
            repeat()
        elif c==5:
            return
        else:
            pass
            repeat()


if __name__ == "__main__":
    repeat()

    





    