#1st Method:
#Function Call within same .py file

def enter_tasks(inputs):
    taskss = []
    taskss.append(inputs)

    return taskss

if __name__ == "__main__":
    task = input("Enter a task: ")
    print(enter_tasks(task))