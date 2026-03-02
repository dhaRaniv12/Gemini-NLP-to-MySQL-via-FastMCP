#3rd Method:
#Rest API Call via FastAPI

import os
from dotenv import load_dotenv
from fastapi import FastAPI
import mysql.connector


app = FastAPI()

load_dotenv()
sql_password = os.getenv('SQL_PW') 

def get_db_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=sql_password,
        database="tasks_test"
    )

@app.get("/tasks")
def get_tasks():
    conn = get_db_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM taskss;")
    taskss = cursor.fetchall()
    cursor.close()
    conn.close()
    return taskss

@app.post("/tasks/{title}")
def create_task(title: str):
    conn = get_db_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO taskss (title) VALUES (%s);", (title,))
    conn.commit()
    print(f"Added new task: {title}")
    cursor.close()
    conn.close()

    return {"message": f"{title} added successfully in db."}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    conn = get_db_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM taskss WHERE id = %s;", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": f"Task {id} deleted successfully."}
    
@app.patch("/tasks/{task_id}/{title}")
def update_task(task_id, title):
    c = get_db_conn()
    cur = c.cursor()
    cur.execute(
        "UPDATE taskss SET title=%s WHERE id=%s",
        (title, task_id)
    )
    c.commit()
    cur.close()
    c.close()
    return {"status": "updated"}




