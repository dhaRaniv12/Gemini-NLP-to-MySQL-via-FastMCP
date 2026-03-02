import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
sql_password = os.getenv('SQL_PW') 

def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=sql_password,
        database="tasks_test"
    )

def get_tasks():
    c = conn()
    cursor = c.cursor(dictionary=True)
    cursor.execute("SELECT * FROM taskss;")
    taskss = cursor.fetchall()
    cursor.close()
    c.close()
    return taskss

def create_task(title: str):
    c = conn()
    cursor = c.cursor(dictionary=True)
    cursor.execute("INSERT INTO taskss (title) VALUES (%s);", (title,))
    c.commit()
    cursor.close()
    c.close()
    return {"message": f"{title} added successfully in db."}

def delete_task(id: int):
    c = conn()
    cursor = c.cursor(dictionary=True)
    cursor.execute("DELETE FROM taskss WHERE id = %s;", (id,))
    c.commit()
    cursor.close()
    c.close()
    return {"message": f"Task {id} deleted successfully."}
    
def update_task(task_id, title):
    c = conn()
    cur = c.cursor()
    cur.execute(
        "UPDATE taskss SET title=%s WHERE id=%s",
        (title, task_id)
    )
    c.commit()
    cur.close()
    c.close()
    return {"message": f"Task {id} updated successfully with {title}."}
