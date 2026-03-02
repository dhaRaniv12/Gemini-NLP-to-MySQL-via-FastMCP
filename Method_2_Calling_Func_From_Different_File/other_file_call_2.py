#2nd Method:
#Function Call with other .py file

import sys
sys.path.insert(1, './Method_1_Calling_Func_Same_File/')

from function_call_1 import enter_tasks

task = input("Enter a task: ")
print(enter_tasks(task))
