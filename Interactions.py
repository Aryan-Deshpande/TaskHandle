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
    task_saved = open('task_saved.json', 'r+')
    saved = json.load(task_saved)
    tasks = saved['activity']
    print(saved)
    print(tasks)
    task_save= tasks[0]
    print(task_save)

    print("enter positions you want to be switched")
    a = input("Enter a")
    b = input("Enter b")
    a1=int(a) -1
    b1=int(b) -1

    
    tempf = tasks[a1]
    temps = tasks[b1]
    print(tasks[a1])
    
    """temp = word1
    word1 = word2
    word2 = temp"""

    temp = tempf.get(a)
    tempf[a]=temps.get(b)
    temps[b]=temp
    print(tempf)
    
    

    task_saved.seek(0)
    json.dump(saved, task_saved, indent=4)
    task_saved.close()

     

        
        





