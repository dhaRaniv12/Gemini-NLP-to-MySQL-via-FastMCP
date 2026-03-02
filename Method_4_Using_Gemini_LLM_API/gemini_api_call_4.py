#4th Method:
#LLM API Call, NO MCP - Only using Gemini API Docs/Schema.

import os
from dotenv import load_dotenv
from google import genai
from llm_tools_mapper import execute_tool

load_dotenv()
apy = os.getenv('API_KEY')

client = genai.Client(api_key = apy)

task_call = [{
    "function_declarations": [
    {
    "name": "insert_task",
    "description": "Create a new task in the task database when user asks to add a task",
    "parameters": {
        "type": "object",
        "properties":{ #inputs needed to insert the task, which is "title" of type "string" and its required.
            "title": {"type":"string"},
        },
        "required":["title"],
    }
    },
    {
    "name": "read_task",
    "description": "Read all task",
    "parameters": { #since its only to read, only prompt to show is enough. no other technical inputs are required.
        "type": "object",
        "properties":{},}
    },
    {
    "name": "delete_task",
    "description": "Delete a task",
    "parameters": {
        "type": "object",
        "properties":{ #inputs needed to delete the task, which is "task_id" of type "integer" and its required.
            "task_id": {"type":"integer"},
        },
        "required":["task_id"],}
    },
    {
    "name": "update_task",
    "description": "Update an existing task",
    "parameters": {
        "type": "object",
        "properties":{ #inputs needed to delete the task, which is "task_id" of type "integer" and its required.
            "task_id": {"type":"integer"},
            "task_title": {"type":"string"}
        },
        "required":["task_id", "task_title"],}
    },
    ]
}]

def chat(prompt):
    response = client.models.generate_content(
        #  model="gemini-2.5-flash",
         model="gemini-3-flash-preview",
         contents = prompt,
         config={
            "tools": task_call
         }
    )

    candidate = response.candidates[0]
    part = candidate.content.parts[0]
    #print("candidate: ", candidate, type(candidate))
    #print("part: ",part, type(part))
    if hasattr(part, "function_call"):
        name = part.function_call.name
        args = dict(part.function_call.args)
        result = execute_tool(name, args)

        print("Tool used: ", name)
        print("Result: ", result)
    else:
        print(response.text)


while True:
    prompt = input("Ask a prompt? (Y to exit.) ")
    if prompt.strip() == 'Y' or prompt.strip() == 'y':
        print("Thanks for using.")
        break;    
    chat(prompt)