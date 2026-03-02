#5th Method:
#Using MCP here, to add n number of tools (functions) without any context
# it automatically decides based on function name & description provided in db_mcp_server
 

import os
from dotenv import load_dotenv
import sys
import asyncio
import json
from google import genai
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession

load_dotenv()
apy = os.getenv('API_KEY')

client = genai.Client(api_key = apy)

async def chat(prompt, session, task_call):
    response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents = prompt,
                config={"tools": task_call}
            )

    candidate = response.candidates[0]
    part = candidate.content.parts[0]
    

    if hasattr(part, "function_call"):
        #print("Executing MCP tool:", part.function_call.name)

        result = await session.call_tool(
            part.function_call.name, 
            dict(part.function_call.args)
            )

        # Iterate over all content elements in the result
        print("\n--- MCP Tool Output ---")
        for content_item in result.content:
            text_result = content_item.text
            try:
                result_data = json.loads(text_result)
                if "title" in result_data:
                    print(f"- {result_data['title']}")
                elif "message" in result_data:
                    print(result_data["message"])
                else:
                    print(result_data)
            except json.JSONDecodeError:
                print(text_result)
        print("-----------------------\n")
    else:
        print(response.text)


async def main():
    server = StdioServerParameters(
        command=sys.executable, 
        args=["Method_5_Using_FastMCP_Gemini_LLM_API/mcp_db_server.py"]
        )


    async with stdio_client(server) as (r,w):
        async with ClientSession(r,w) as session:
            await session.initialize()

            mcp_tools = await session.list_tools()
            #print(f"MCP TOOLS: {mcp_tools}")

            task_call = [{
                "function_declarations": [
                    {
                        "name": t.name,
                        "description": t.description or "MCP tool",
                        "parameters": t.inputSchema
                    }
                    for t in mcp_tools.tools
                ]
            }]

            print("Server connected successfully! You can now start chatting.")
            while True:
                prompt = input("\nAsk a prompt? (Y to exit.) ")
                if prompt.strip() == 'Y' or prompt.strip() == 'y':
                    print("Thanks for using.")
                    break  
                
                await chat(prompt, session, task_call)

    
asyncio.run(main())