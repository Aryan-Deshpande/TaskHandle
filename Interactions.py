import itertools
import json


def add_task(filename='task_saved.json'):

#   opened the json file using read and append mode
    task_saved = open(filename, 'r+')

#   json.load converts json string --> to a python dictionary
#   saved is a dict containing json info
    saved = json.load(task_saved)

#   this size_of_tasks stores the length of the python dict
    size_of_tasks=len(saved['activity'])

#   creating temperory dict, to get input from the user and add task
    temp_dict = dict()
    temp_dict[(size_of_tasks+1)] = input("Enter the task\n")

#   appends temp dict into saved dict
    saved['activity'].append(temp_dict)
    #print(type(saved['activity']))

    """
    0: sets the reference point at the beginning of the file. 
    1: sets the reference point at the current file position.
    2: sets the reference point at the end of the file.
    """
    task_saved.seek(0)
    #print(saved)
#   converts python dict to json string
    json.dump(saved,task_saved,indent=4)

    task_saved.close()

    

def read_task(filename='task_saved.json'):
    task_saved = open(filename,'r') # _io.TextIOWrapper
    saved = json.load(task_saved)   # dict
    tasks = saved['activity']       # list

    for i in range(len(tasks)):
        temp_dict = tasks[i]
        for k,v in temp_dict.items():
            print(k+")",v)



def delete_task(filename='task_saved.json'):
    task_saved = open(filename,'r+')
    saved = json.load(task_saved)
    tasks = saved['activity']

    print("Enter the priority you want deleted")
    task_delete = input()

    temp_key = ""

    for i in range(0,len(tasks)):
        temp_dict = tasks[i]

        for k,v in temp_dict.items():
            #print("in kv loop")
            print(type(k))
            print(k,v)
            temp_key = k

        if temp_key == task_delete:
            tasks.remove(temp_dict)
            #print("removing")
            #print(tasks) 
            break

   #print(saved['activity'])
    #saved['activity'] = tasks
    print(saved['activity'])
    #saved['activity'].write(task_saved)
    
    #task_saved.seek(0)
    #a = {'activity':[{'5':'sleep'}]}
    for i in range(0,len(saved['activity'])):
        t_dict=tasks[i]
        for k,v in t_dict.items():
            k = i


    b = json.dumps(saved,indent=4)
    open('task_saved.json','w').write(b)

    task_saved.close()
    task_saved.close()

def inbetween():
    task_saved = open ('task_savd.json', 'r+')
    saved = json.load(task_saved)

     

        
        





