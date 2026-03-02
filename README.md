# LLM + REST API + MySQL + FastMCP Learning Project

This project is a hands-on implementation to understand:

-   LLM API integration from scratch (Gemini)
-   REST API development using FastAPI
-   MySQL CRUD operations
-   Tool calling architecture
-   FastMCP for reducing LLM boilerplate code

Each concept is implemented as an **independent method** for
step-by-step learning.

------------------------------------------------------------------------

# 📂 Project Structure

    Gemini-NLP-to-MySQL-via-FastMCP-main

    ├── Method_1_Calling_Func_Same_File/
    │   └── function_call_1.py
    │
    ├── Method_2_Calling_Func_From_Different_File/
    │   └── other_file_call_2.py
    │
    ├── Method_3_Using_RestAPI_to_CRUD_Data/
    │   └── fastapi_rest_api_method_call_3.py
    │
    ├── Method_4_Using_Gemini_LLM_API/
    │   ├── sql_database_tools_funcs.py
    │   ├── gemini_api_call_4.py
    │   ├── gemini_llm_just_chat.py
    │   └── llm_tools_mapper.py
    │
    ├── Method_5_Using_FastMCP_Gemini_LLM_API/
    │   ├── db_tools_mcp.py
    │   ├── gemini_mcp_client_5.py
    │   └── mcp_db_server.py
    │
    ├── .env.example
    ├── .gitignore
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# ⚙️ Setup Instructions

## 1️⃣ Clone the repository

``` bash
git clone https://github.com/dhaRaniv12/Gemini-NLP-to-MySQL-via-FastMCP.git
cd Gemini-NLP-to-MySQL-via-FastMCP-main
```

------------------------------------------------------------------------

## 2️⃣ Create virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

------------------------------------------------------------------------

## 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 4️⃣ Configure environment variables

Create a `.env` file based on `.env.example`:

    API_KEY='YOUR_GEMINI_API_KEY'
    SQL_PW = "YOUR_MySQL_PW"

------------------------------------------------------------------------

# 🎯 Learning Flow

## Method 1 -- Function Call (Same File)

Goal: - Understand basic Python function execution - Control flow inside
a single script

Run:

``` bash
python Method_1_Calling_Func_Same_File/function_call_1.py
```

------------------------------------------------------------------------

## Method 2 -- Function Call (Different File)

Goal: - Learn modular programming - Use imports and separation of logic
across files

Run:

``` bash
python Method_2_Calling_Func_From_Different_File/other_file_call_2.py
```

------------------------------------------------------------------------

## Method 3 -- FastAPI REST API + MySQL (CRUD)

Goal: - Build REST endpoints - Perform Create, Read, Update, Delete
operations on MySQL - Test APIs using Swagger UI

Run server:

``` bash
fastapi dev Method_3_Using_RestAPI_to_CRUD_Data/fastapi_rest_api_method_call_3.py
```

Open Swagger docs:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Method 4 -- Gemini LLM API (NLP → DB Operations)

Features:

-   Accept natural language input
-   Convert NLP → structured database operation
-   Execute MySQL queries via `db_tools.py`
-   Tool execution handled by `tool_executor.py`
-   `gemini_llm_just_chat.py` for basic chat testing

Run:

``` bash
python Method_4_Using_Gemini_LLM_API/gemini_api_call_4.py
```

Example input:

    Add a task at tomorrow 3pm to order groceries

------------------------------------------------------------------------

## Method 5 -- FastMCP + Gemini

Goal:

-   Eliminate redundant tool-calling logic from Method 4
-   Use FastMCP for standardized tool execution
-   Improve maintainability and architecture

Run:

``` bash
python Method_5_Using_FastMCP_Gemini_LLM_API/gemini_mcp_client_5.py
```

------------------------------------------------------------------------

# 🧱 Tech Stack

-   Python
-   FastAPI
-   MySQL
-   google-genai (Gemini API)
-   FastMCP

------------------------------------------------------------------------

# 👨‍💻 Purpose

This is a **learning-focused backend + LLM integration project**
designed to understand real-world architecture step by step, from basic
Python function calls to LLM-driven database operations.
