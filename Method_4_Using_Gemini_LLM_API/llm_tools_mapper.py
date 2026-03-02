from sql_database_tools_funcs import get_tasks, create_task, delete_task, update_task

def execute_tool(name, args):
    if name == 'read_task':
        return get_tasks()
    if name == 'insert_task':
        print(args["title"])
        return create_task(args['title'])
    if name == 'delete_task':
        return delete_task(args['task_id'])
    if name == 'update_task':
        return update_task(args['task_id'], args['task_title'])