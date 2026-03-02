from mcp.server.fastmcp import FastMCP
from db_tools_mcp import get_tasks, create_task, delete_task, update_task

mcp = FastMCP("insert-taskss")

@mcp.tool()
def get_tasks_tool():
    """Retrieves all tasks from the MySQL database."""
    return get_tasks()

@mcp.tool()
def create_task_tool(title: str):
    """Creates a new task in the database with the given title."""
    return create_task(title)

@mcp.tool()
def delete_task_tool(task_id: int):
    """Deletes an existing task from the database by its task_id."""
    return delete_task(task_id)

@mcp.tool()
def update_task_tool(task_id: int, title: str):
    """Updates the title of an existing task in the database."""
    return update_task(task_id, title)


if __name__ == "__main__":
    import sys
    print("Starting MCP Server...", file=sys.stderr)
    mcp.run()
